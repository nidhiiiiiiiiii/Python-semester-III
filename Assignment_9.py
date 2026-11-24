import csv
import json
from pathlib import Path


def csv_to_json(csv_path: str | Path, json_path: str | Path, indent: int = 4) -> list[dict[str, str]]:
    """Read rows from a CSV file and write them as a JSON array of objects."""
    source = Path(csv_path)
    destination = Path(json_path)

    if not source.is_file():
        raise FileNotFoundError(f"CSV file not found: {source}")

    with source.open(mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError(f"CSV file is empty or missing a header row: {source}")
        records = [row for row in reader]

    # Ensure parent directories exist if a nested path is provided
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open(mode="w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=indent, ensure_ascii=False)

    return records


def main() -> None:
    sample_csv = Path("students.csv")
    output_json = Path("students.json")

    # Create a small sample CSV so the script runs immediately if you don't have one ready
    if not sample_csv.exists():
        sample_csv.write_text(
            "id,name,course,score\n"
            "101,Aarav Sharma,Computer Science,88\n"
            "102,Priya Nair,Data Science,92\n"
            "103,Rohan Verma,Electronics,79\n",
            encoding="utf-8",
        )

    records = csv_to_json(sample_csv, output_json)
    print(f"Converted {len(records)} rows from '{sample_csv}' to '{output_json}'.")
    print(json.dumps(records, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()