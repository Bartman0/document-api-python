try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tableaudocumentapi',
    version='0.10',
    author='Richard Kooijman',
    author_email='rkooijman@quicknet.nl',
    url='https://github.com/Bartman0/document-api-python',
    packages=['tableaudocumentapi'],
    license='MIT',
    description='A Python module for working with Tableau files.',
    test_suite='test'
)
