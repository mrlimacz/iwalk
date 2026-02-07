import logging
from pathlib import Path
from os import walk
import polars as pl
from exiftool import ExifToolHelper
from iwalk.constants import EXCLUDED_TYPES, EXIF_TAGS, SUPPORTED_ASSET_TYPES

logger = logging.getLogger(__name__)


def _validate_input_path(path: Path) -> None:
    if not path.is_dir():
        raise FileNotFoundError(f"{path} is not a directory")
    logger.debug(f"{path} exists and is a directory")


def _walk_files(path: Path) -> pl.DataFrame:
    df = (
        pl.DataFrame(walk(path), schema=["root", "dirs", "file"])
        .explode("file")
        .drop_nulls("file")
    )

    df = df.select(
        "root",
        "file",
        pl.struct(["root", "file"])
        .map_elements(lambda x: Path(x["root"], x["file"]))
        .alias("file_path"),
    )
    df = df.with_columns(
        pl.col("file_path")
        .map_elements(
            lambda x: x.parent.relative_to(path).as_posix(), return_dtype=pl.String
        )
        .alias("dir")
    )
    logger.info(f"Found {df.height} files")
    return df


def _extract_file_attributes(df: pl.DataFrame) -> pl.DataFrame:
    df = df.with_columns(
        pl.col("file_path")
        .map_elements(lambda x: x.suffix, return_dtype=pl.String)
        .alias("suffix"),
        pl.col("file_path")
        .map_elements(lambda x: x.stem, return_dtype=pl.String)
        .str.extract_groups(
            r"^(?P<obj_1>IMG_)(?P<obj_type>O|E)?(?P<obj_2>\d{4})$|^(?P<name>.*)$"
        )
        .alias("match_groups"),
    )
    df = df.select(
        pl.all().exclude("suffix", "match_groups"),
        pl.col("match_groups")
        .struct.field("obj_1")
        .is_not_null()
        .alias("is_patterned"),
        pl.when(pl.col("match_groups").struct.field("obj_1").is_not_null())
        .then(
            pl.col("match_groups").struct.field("obj_1")
            + pl.col("match_groups").struct.field("obj_2")
        )
        .otherwise(pl.col("match_groups").struct.field("name"))
        .alias("obj_name"),
        (
            pl.col("match_groups").struct.field("obj_type").fill_null("O")
            + pl.col("suffix").str.to_uppercase().str.replace(r"^JPEG$", "JPG")
        ).alias("obj_type"),
    )
    df = df.filter(~pl.col("obj_type").is_in(EXCLUDED_TYPES))
    logger.info(f"Excluding {EXCLUDED_TYPES}, remaining {df.height} files")
    return df


def _extract_exif_data(df: pl.DataFrame, skip_exif: bool) -> pl.DataFrame:
    if skip_exif:
        logger.info("Skipping exif extraction")
        df = df.with_columns(
            [pl.lit(None).cast(pl.String).alias(exif_tag) for exif_tag in EXIF_TAGS]
        )
    else:
        logger.info(f"Extracting {EXIF_TAGS} from exif")
        with ExifToolHelper(common_args=["-n"], check_execute=False) as eth:
            df = df.with_columns(
                pl.col("file_path")
                .map_elements(
                    lambda s: eth.get_tags(s.as_posix(), tags=EXIF_TAGS)[0],
                    return_dtype=pl.Struct({c: pl.String for c in EXIF_TAGS}),
                )
                .alias("tags")
            )
            df = df.select(pl.all().exclude("tags"), pl.col("tags").struct.unnest())
            for tag in EXIF_TAGS:
                check = (
                    df.filter(pl.col(tag).is_not_null())
                    .group_by(tag)
                    .agg(
                        pl.col("file").len().alias("file_count"),
                        pl.col("file").implode().list.join(", ").alias("file_list"),
                    )
                )
                if check.height > 0:
                    logger.info(f"Found {check.height} of {tag}: {check}")
    return df


def run_iwalk(path: Path, skip_exif: bool) -> list[str] | None:
    logger.info(f"Analyzing files in {path.as_posix()}")

    # Validate input path
    _validate_input_path(path)

    # Walk and parse to df
    df = _walk_files(path)

    # extract obj names
    df = _extract_file_attributes(df)

    # run exif
    df = _extract_exif_data(df, skip_exif)

    # Group results

    # Validate

    return None
