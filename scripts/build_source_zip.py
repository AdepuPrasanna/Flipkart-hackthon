"""Build gridlock_source_submission.zip with all 6 required files at archive root."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source_submission"
ZIP_PATH = ROOT / "gridlock_source_submission.zip"

FILES = [
    "ZIP_MANIFEST.txt",
    "approach.txt",
    "predict.py",
    "requirements.txt",
    "README.txt",
    "traffic_demand_solution.ipynb",
    "Gridlock_Presentation.pptx",
]


def main():
    missing = [f for f in FILES if not (SRC / f).exists()]
    if missing:
        raise SystemExit(f"Missing in source_submission/: {missing}")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in FILES:
            path = SRC / name
            zf.write(path, arcname=name)
            print(f"  + {name} ({path.stat().st_size} bytes)")

    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        names = zf.namelist()
        assert names == FILES, f"Zip manifest mismatch: {names}"
        for name in FILES:
            info = zf.getinfo(name)
            assert info.file_size > 0, f"Empty entry: {name}"

    print(f"\nOK: {ZIP_PATH} ({ZIP_PATH.stat().st_size} bytes)")
    print("Contents:", names)

    downloads = Path.home() / "Downloads" / "gridlock_source_submission.zip"
    downloads.write_bytes(ZIP_PATH.read_bytes())
    print(f"Copied -> {downloads}")


if __name__ == "__main__":
    main()
