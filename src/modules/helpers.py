from typing import Dict
import os
import json


def save_url(imglink: str, filepath: str) -> None:
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(imglink + "\n")


def save_metadata(metadata: Dict[str, str], filepath: str) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(metadata, f)


def clean_temp_folder(pattern_page) -> None:
    os.system(f"rm -r {pattern_page}")
