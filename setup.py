from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyroborock',
    version='1.1.3',
    packages=['pyroborock'],
    install_requires=['tinytuya==v1.2.11', 'python-miio==0.5.9.2', 'pycryptodome==3.9.8'],
    description='Communicate with roborock over tuya protocol',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/nathanfiscus/pyroborock',
    author='nathanfiscus',
    author_email='nathan_fiscus@hotmail.com',
)
