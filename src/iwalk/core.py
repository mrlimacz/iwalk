import logging
from pathlib import Path
from os import walk
import polars as pl

logger = logging.getLogger(__name__)


def _validate_input_path(path: Path) -> None:
    if not path.is_dir():
        raise FileNotFoundError(f"{path} is not a directory")


def _walk_files(path: Path) -> pl.DataFrame:
    df = pl.DataFrame(walk(path), schema=["root", "dirs", "file"])
    df = df.with_columns(
        pl.col("root")
        .map_elements(
            lambda x: Path(x).relative_to(path).as_posix(), return_dtype=pl.String
        )
        .alias("dir")
    )
    df = df.explode("file").drop_nulls("file").select(["root", "dir", "file"])
    return df


def run_iwalk(path: Path) -> list[str] | None:
    # Validate input path
    _validate_input_path(path)

    # Walk and parse to df
    df = _walk_files(path)

    # extract obj names

    # run exif

    # Group results

    # Validate

    return None
