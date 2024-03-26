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

    # def test_empty_name(self):
    #     pass
    #
    # def test_empty_packages_data(self):
    #     pass
    #
    # def test_invalid_packages_data(self):
    #     pass
    #
    # def test_empty_packages_data_empty_name(self):
    #     pass
    #
    # def test_unsuccessful_find(self):
    #     pass
