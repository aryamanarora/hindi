from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hindi',
    version='0.0.0',
    description='Useful tools for dealing with Hindi',
    long_description=readme,
    author='Aryaman Arora',
    author_email='aryaman.arora2020@gmail.com',
    url='https://github.com/aryamanarora/hindi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
