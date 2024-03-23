from typing import List, Dict
from constants import SOURCES_DIR
import os
import json


def get_packages_dirs(path: str = SOURCES_DIR) -> Dict[str, str]:
    packages = os.listdir(path)
    for package in packages:
        print(package)
    return {}


def get_appman_data(name: str) -> List[str]:
    packages = get_packages_dirs()
    return []


def main():
    print(SOURCES_DIR)


if __name__ == "__main__":
    main()
