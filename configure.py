import os
import shutil
from pathlib import Path


def main() -> None:
    # source files look for cddlib/*.h
    # so copy headers to cddlib/... folder
    src_dir = Path("src/cddlib/lib-src")
    dest_dir = Path("src/include/cddlib")
    dest_dir.mkdir(parents=True, exist_ok=True)
    for file in src_dir.glob("*.h"):
        shutil.copy(file, dest_dir)
    # remove gmp.pyi (otherwise setuptools includes it even with explicit exclude...)
    try:
        os.remove("src/pycddlib/src/cdd/gmp.pyi")
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
