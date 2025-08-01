from setuptools import setup,find_packages 
from typing import List 
import os 


def get_requirements()->List[str]: 
    requirements_list:List[str]=[]
    try: 
        with open("requirements.txt","r") as f: 
            lines=f.readlines() 
            for line in lines: 
                requirement=line.strip() 
                if requirement and requirement != "-e .": 
                    requirements_list.append(requirement)
    except FileNotFoundError: 
        print("requirements.txt not found......")
    
    return requirements_list 

setup( 
    version="0.0.1", 
    author="Mayur", 
    packages=find_packages(), 
    install_requires=get_requirements()
)
