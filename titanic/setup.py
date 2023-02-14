from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = [
    'gcsfs==0.7.1', 
    'google-cloud-bigquery-storage==1.0.0', 
    'six==1.15.0',
    'google-auth-oauthlib==0.5.3',
    'google-api-core==1.23.0'
]

 
setup(
    name='trainer', 
    version='0.1', 
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(), # Automatically find packages within this directory or below.
    include_package_data=True, # if packages include any data files, those will be packed together.
    description='Classification training titanic survivors prediction model'
)