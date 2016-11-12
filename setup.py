from setuptools import setup, find_packages


with open('README.md') as f:
    readme_content = f.read()

with open('LICENSE') as f:
    license_content = f.read()

setup(
    name='metaconfig',
    version='0.1',
    description='Configuration tool for configuration files',
    long_description=readme_content,
    author='Renat Zhilkibaev',
    author_email='rzhilkibaev@gmail.com',
    url='https://github.com/rzhilkibaev/metaconfig',
    license=license_content,
    packages=find_packages(exclude=('tests', 'docs'))
)