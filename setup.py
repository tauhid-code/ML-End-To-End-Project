from setuptools import setup, find_packages
from typing import List
def get_requirement(file_path:str)->list:
    """This function will return the list of requirements"""
    with open(file_path) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        
        if '-e .' in requirement_list:
            requirement_list.remove('-e .')
    
    return requirement_list


setup(
    name = "MLProject",
    version = "0.0.1",
    author= "Tauhid Ur Rehman",
    author_email="tauhidurrehman7@gmail.com",
    packages=find_packages(),
    ## Create a function because it is not feasible to add each and every library
    install_requires=get_requirement('requirements.txt')

)