from typing import List
from setuptools import find_packages, setup




def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the List of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[item.replace("\n","") for item in requirements]
       # if '-e .' in requirements:
            #requirements.remove('-e .')
    
    return requirements

setup(
name ='ml-project 4',
versions = '0.0.5',
author = 'Rowland',
author_email = 'oshiotserowland@gmail.com',
packages =find_packages(),
install_requires = get_requirements('requirements.txt')    
)