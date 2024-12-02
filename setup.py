from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='Speech_to_Text',
    version='0.0.1',
    author='Kaustubh',
    author_email='karanje.kaustubh23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A speech-to-text conversion project using ML',
    license='MIT',
    url='https://github.com/Kaustubh-Data-Scientist/Speech_to_Text',

)