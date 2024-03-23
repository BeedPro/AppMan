import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from appman.sources import get_packages


class TestGetPackages(unittest.TestCase):
    def test_success_package(self):
        pass

    def test_invalid_path(self):
        pass

    def test_empty_string_paramater(self):
        pass

    def test_non_string_parameter(self):
        pass
