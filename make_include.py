import shutil
from pathlib import Path


def main() -> None:
    src_dir = Path("cddlib/lib-src")
    dest_dir = Path("include/cddlib")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for file in src_dir.glob("*.h"):
        shutil.copy(file, dest_dir)


if __name__ == '__main__':
    main()
