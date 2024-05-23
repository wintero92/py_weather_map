import json
import re
from pathlib import Path


def normalize_name(name: str) -> str:
    name = re.sub(r"[^a-zA-Z_ ]", " ", name)
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r" ", "_", name)
    name = re.sub(r"-", "_", name)
    return name.upper()


def main() -> None:
    with Path.open(Path("data/nominatim.json"), mode="r", encoding="utf-8") as file:
        data = json.load(file)
    english_names = [item["english"] for item in data["nominatim"]]
    enum_content = []
    for english_name in english_names:
        normalized_english_name = normalize_name(english_name)
        enum_content.append(f'{normalized_english_name} = "{english_name}"')
    enum_content = sorted(enum_content)

    with Path.open(Path("data/nominatim.py"), mode="w", encoding="utf-8") as file:
        file.write("from enum import StrEnum\n")
        file.write("class Nominatim(StrEnum):\n")
        for enum_item in enum_content:
            file.write(f"  {enum_item}\n")


if __name__ == "__main__":
    main()
