from setuptools import setup, find_packages

setup(
   name='Money',
   version='0.1',
   description='To Learn About Last Currencies',
   author='Abdul Akhundzade (C)Baku, AZ',
   license='MIT',
   install_requires=['click', 'requests'],
   py_modules=['money'],
   packages=find_packages(),
   include_package_data=True
)
