from setuptools import setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Jobin Mathew"
DESCRIPTION = "This is the first FSDS Nov batch Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """
    :Function Name: get_requirements_list
    :Description: This function is going to return list of requirements mentioned in the requirements.txt file

    :returns: List Containing Requirements for the project
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())