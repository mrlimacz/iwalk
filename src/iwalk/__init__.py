import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Walk over photos and videos transferred via gphoto2 and select relevant to upload"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=Path.cwd(),
        type=Path,
        help="Directory path (defaults to current directory)"
    )

    args = parser.parse_args()

    print("Hello from iwalk!")

if __name__ ==  "__main__":
    main()
    