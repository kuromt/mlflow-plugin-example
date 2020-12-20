
import os, sys
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirementes = [
    'mlflow',
]
    
setup(
    name='mlflow-plugin-example',
    version='0.0.1',
    description='mlops plugin example',
    long_description=readme,
    author='kuromt',
    author_email='n.kuromatsu@gmail.com',
    install_requires=requirementes,
    url='https://github.com/kuromt/mlflow-plugin-example',
    license=license,
    entry_points={
        'mlflow.run_context_provider': 'plugin_example=plugin_example.logging_example:LoggingExample',
    },
    packages=find_packages(),
)