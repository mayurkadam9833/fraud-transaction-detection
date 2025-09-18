import os 
from setuptools import setup,find_packages 
from typing import List 


# This function read requirements.txt file return dependencies and packages required for project
def get_requirements()-> List[str]:
    requirements_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt not found")
    
    return requirements_lst

# Setup configuration for the package
setup(
    version="0.0.1",
    author="Mayur",
    packages=find_packages(),             # Automatically finds all Python packages
    install_requires=get_requirements()   # Installs dependencies from requirements.txt 
)
