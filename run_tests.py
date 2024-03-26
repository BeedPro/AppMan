#!/usr/bin/env python3

import unittest
import os
import sys


def get_dirs(test_dir):
    if not os.path.isdir(test_dir):
        exit(f"Error: No such directory: {test_dir}")

    dirs = []
    for item in os.listdir(test_dir):
        is_dir = os.path.isdir(os.path.join(test_dir, item))
        if item == "__pycache__" or item.startswith("."):
            continue
        if is_dir:
            dirs.append(item)
    return dirs


def get_tests(dir):
    tests = []
    for item in os.listdir(dir):
        if item == "__pycache__" or item.startswith("."):
            continue
        tests.append(item)
    return tests


def get_all_tests(test_dir):
    all_tests = {}
    dirs = get_dirs(test_dir)
    for dir in dirs:
        tests = get_tests(os.path.join(test_dir, dir))
        all_tests = {dir: tests}

    return all_tests


def run_tests(dir, pattern="test_*.py"):
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(dir, pattern=pattern)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


def run(args=sys.argv[1:]):
    test_dir = "tests"
    tests = get_all_tests(test_dir)

    if args:
        for arg in args:
            split_args = arg.split(".")
            dir = split_args[0]
            test_pattern = (
                f"test_{split_args[1]}.py" if len(split_args) > 1 else "test_*.py"
            )
            formated_dir = os.path.join(test_dir, dir)
            run_tests(formated_dir, test_pattern)

    else:
        print("Running all tests")
        for dir in tests:
            formated_dir = os.path.join(test_dir, dir)
            run_tests(formated_dir)


if __name__ == "__main__":
    run()
