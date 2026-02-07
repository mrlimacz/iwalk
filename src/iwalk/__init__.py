import argparse
from pathlib import Path
import logging
from iwalk.core import run_iwalk

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(message)s")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Walk over photos and videos transferred via gphoto2 and select relevant to upload"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=Path.cwd(),
        type=Path,
        help="Directory path (defaults to current directory)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Use more detailed logging"
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    setup_logging(args.verbose)
    run_iwalk(path=args.path)


if __name__ == "__main__":
    main()
