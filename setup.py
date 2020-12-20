
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
    description='mlops plugin demo',
    long_description=readme,
    author='kuromt',
    author_email='n.kuromatsu@gmail.com',
    install_requires=requirementes,
    url='https://github.com/kuromt/sanfrancisco_house',
    license=license,
    entry_points={
        'mlflow.run_context_provider': 'plugin_example:LoggingPlugin',
    },
    packages=find_packages(),
    include_package_data=True,
)