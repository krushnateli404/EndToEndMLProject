from setuptools import setup
from typing import List


PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR  = "Krushna Teli"
DESCRIPTION = "This is a house price prediction machine learnin project"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirement_list()->List[str]:
    """Description : this function is going to list of requirement mention in requirements.txt file
    
    return: this function is going to return a list which contain name of libraries mention in requirements.txt file """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readline()






setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_require = get_requirement_list()
    
)


# if __name__ == "__main__":
#     print(get_requirement_list())