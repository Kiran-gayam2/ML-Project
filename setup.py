from setuptools import setup
from typing import List

# declaring variables for setup function
project_Name = 'housing_predictor'
Version = '0.0.1'
Author = 'kiran'
Description = 'Machine learning project'
Packages = ['housing']
Requirements_file_name = 'requirements.txt'



def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements in rewuirements.txt file

    return function gives a list which contains name of libraries mentioned in requirement.txt
    """

    with open(Requirements_file_name) as require_file:
        return require_file.readlines()

setup(
    name = project_Name,
    version = Version,
    author = Author,
    description=Description,
    package = Packages,
    install_requires=get_requirements_list() 
)


if __name__=="__main__":
    print(get_requirements_list())