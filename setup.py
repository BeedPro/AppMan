from setuptools import setup, find_packages

# Project metadata
NAME = "Your_Project_Name"
DESCRIPTION = "Brief description of your project"
URL = "https://github.com/BeedPro/AppMan"
EMAIL = "youremail@example.com"
AUTHOR = "Your Name"
REQUIRES_PYTHON = ">=3.11.0"
VERSION = "0.1.0"

# Required packages
REQUIRED = [
    "package1",
    "package2",
    # Add any other dependencies here
]

# Additional packages to include, if any
EXTRAS = {
    # 'extra_feature': ['package3', 'package4'],
}

# Long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="GPL",  # GNU GENERAL PUBLIC LICENSE
    classifiers=[
        # Trove classifiers
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
