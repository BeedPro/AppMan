from typing import List, Dict
from appman.constants import SOURCES_DIR
import os


# TODO: Add tests to tests/sources
def get_packages(path: str = SOURCES_DIR) -> List[Dict]:
    """
    Get the list of packages in the source directory
        Parameters:
            path (str): The path to the source directory, Default: SOURCES_DIR
        Returns:
            packages (List): The list of packages in the source directory
    """
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


# TODO: Add tests to tests/sources
def get_package(name: str, packages_data: List[Dict]) -> Dict[str, str]:
    """
    Get the package data from the packages_data list
        Parameters:
            name (str): The name of the package
            packages_data (List): The list of packages data
        Returns:
            package (Dict): The package data
    """
    for package in packages_data:
        if package["name"] == name:
            return package
    return {}


# TODO: Add tests to tests/sources
def format_script(script: Dict) -> Dict:
    """
    For a given script return the formated data of the placeholder texts within the script
        Parameters:
            script (Dict): The script data
        Returns:
            script (Dict): The formated script data
    """
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


# TODO: Add tests to tests/sources
def read_script(package_name: str, filename: str) -> Dict:
    """
    Read the script file and return the formated data
        Parameters:
            package_name (str): The name of the package
            filename (str): The name of the script file
        Returns:
            script (Dict): The formated script data
    """
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


# TODO: Add tests to tests/sources
def get_appman_data(name: str) -> Dict[str, str]:
    """
    Get the appman data for the given package name
        Parameters:
            name (str): The name of the package
        Returns:
            script (Dict): The script data from the appman file
    """
    package = get_package(name, get_packages())
    script = read_script(package["name"], package["script"])
    return script


def main():
    print(SOURCES_DIR)


if __name__ == "__main__":
    main()
