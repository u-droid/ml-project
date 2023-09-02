from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path: str) -> List[str]:
    requirements = []
    file = open(path)
    requirements = file.readlines()
    requirements = [req.replace('\n','') for req in requirements]
    file.close()
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ujjwal Tyagi',
    author_email='u.tyagi2013@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)