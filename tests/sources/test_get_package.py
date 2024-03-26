from typing import Dict, List
import unittest
from appman.sources import get_package


class TestGetPacakge(unittest.TestCase):
    def test_successful_find(self):
        # Arrange
        name: str = "target_package"
        packages_data: List[Dict] = [
            {"name": "target_package"},
            {"name": "package1"},
            {"name": "package2"},
            {"name": "package3"},
        ]
        expected: Dict[str, str] = {"name": "target_package"}

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_unsuccessful_find(self):
        # Arrange
        name: str = "not_in_packages"
        packages_data: List[Dict] = [
            {"name": "package1"},
            {"name": "package2"},
            {"name": "package3"},
        ]
        expected: Dict[str, str] = {}

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_duplicates_in_packages(self):
        # Arrange
        name: str = "dual_package"
        packages_data: List[Dict] = [
            {"name": "package1", "data": "package_data1"},
            {"name": "package2", "data": "package_data2"},
            {"name": "package3", "data": "package_data3"},
            {"name": "dual_package", "data": "packages_data_dual"},
            {"name": "dual_package", "data": "packages_data_dual"},
        ]
        expected: Dict[str, str] = {
            "name": "dual_package",
            "data": "packages_data_dual",
        }

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_get_first_instance_of_data(self):
        # Arrange
        name: str = "dual_package"
        packages_data: List[Dict] = [
            {"name": "package1", "data": "package_data1"},
            {"name": "package2", "data": "package_data2"},
            {"name": "package3", "data": "package_data3"},
            {"name": "dual_package", "data": "packages_data_dual1"},
            {"name": "dual_package", "data": "packages_data_dual2"},
        ]
        expected: Dict[str, str] = {
            "name": "dual_package",
            "data": "packages_data_dual1",
        }

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_empty_name(self):
        # Arrange
        name: str = ""
        packages_data: List[Dict] = [
            {"name": "package1"},
            {"name": "package2"},
            {"name": "package3"},
        ]
        expected: Dict[str, str] = {}

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_empty_packages_data(self):
        # Arrange
        name: str = "package"
        packages_data: List[Dict] = []
        expected: Dict[str, str] = {}

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)

    def test_invalid_packages_data(self):
        # Arrange
        name: str = "package"
        packages_data: List[Dict] = [{"not_name": "package"}]
        expected: Dict[str, str] = {}

        # Act/Assert
        with self.assertRaises(KeyError) as context:
            result: Dict[str, str] = get_package(name, packages_data)
        self.assertEqual(str(context.exception), "'name'")

    def test_empty_packages_data_empty_name(self):
        # Arrange
        name: str = ""
        packages_data: List[Dict] = []
        expected: Dict[str, str] = {}

        # Act
        result: Dict[str, str] = get_package(name, packages_data)

        # Assert
        self.assertDictEqual(result, expected)
