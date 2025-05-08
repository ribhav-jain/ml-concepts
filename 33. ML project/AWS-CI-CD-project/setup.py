"""
setup.py

This script is used for packaging and distributing the Python project.
It defines the project metadata and dependencies required for installation.

In large-scale machine learning or data science projects, this file ensures:
- Easy project setup via `pip install .` or `python setup.py install`
- Dependency tracking via `requirements.txt`
- Clean project packaging using setuptools
- Compatibility with tools like PyPI, Docker, CI/CD, etc.

Usage:
    $ pip install .
    or
    $ python setup.py install

This file is essential for making the project reusable and shareable.
"""

from setuptools import find_packages, setup
from typing import List

# Constant used to filter out editable installs from requirements
HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: A cleaned list of package dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters and remove empty lines
        requirements = [req.strip() for req in requirements if req.strip()]

        # Remove the editable install line if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# Setup configuration for the ML project
setup(
    name="student_score_predictor",  # Project name
    version="0.1.0",  # Semantic versioning
    author="Ribhav Jain",  # Author name
    author_email="ribhavjain4@gmail.com",  # Author contact
    description="A machine learning project to predict student scores",
    packages=find_packages(
        exclude=["tests", "notebooks"]
    ),  # Automatically find modules
    install_requires=get_requirements("requirements.txt"),  # Install dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Minimum Python version supported
)
