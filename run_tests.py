#!/usr/bin/env python3

import unittest


def run_tests_sources():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests/sources", pattern="test_*.py")
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


if __name__ == "__main__":
    run_tests_sources()
