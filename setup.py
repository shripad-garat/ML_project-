from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file:str):
    """
    This function will going to returns the list of required packges to be install
    """
    with open(file,"r") as intance:
        requirement = intance.readlines()
        requirement = [require.replace('\n',"") for require in requirement]
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement

setup(
    name="ML_Basic_structure_project",
    version="0.0.1",
    author="Shripad Garat(SAG)",
    author_email="garatshripad09@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)

