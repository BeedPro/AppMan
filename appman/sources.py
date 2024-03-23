from typing import List, Dict
from constants import SOURCES_DIR
import os
import json


def get_packages(path: str = SOURCES_DIR) -> List[Dict]:
    packages_in_source = os.listdir(path)
    packages_data = []
    for package in packages_in_source:
        appman_script_files = os.listdir(os.path.join(SOURCES_DIR, package))
        if not len(appman_script_files) == 1:
            raise Exception(
                f"There must be only one appman script in packages/{package}"
            )
        packages_data.append({"name": package, "script": appman_script_files[0]})
    return packages_data


def get_package(name: str, packages_data) -> Dict[str, str]:
    for package in packages_data:
        if package["name"] == name:
            return package
    return {}


def format_script(script: Dict) -> Dict:
    for script_key in script.keys():
        match script_key:
            case "url":
                script[script_key] = script[script_key].format(
                    version=script["version"]
                )

            case "repository":
                script[script_key] = script[script_key].format(url=script["url"])
            case "checksum":
                script[script_key] = script[script_key].format(
                    hash=script["hash"], version=script["version"]
                )
    return script


def read_script(package_name: str, filename: str) -> Dict:
    script_data = {}
    path = f"{SOURCES_DIR}/{package_name}/{filename}"
    with open(path, "r") as script_file:
        data = script_file.readlines()
    for line in data:
        if line.startswith("#"):
            continue
        split_line = line.split("=")
        key = split_line[0]
        value = split_line[1].strip()
        script_data[key] = value
    return format_script(script_data)


def get_appman_data(name: str) -> Dict[str, str]:
    package = get_package(name, get_packages())
    script = read_script(package["name"], package["script"])
    return script


def main():
    print(SOURCES_DIR)


if __name__ == "__main__":
    main()
