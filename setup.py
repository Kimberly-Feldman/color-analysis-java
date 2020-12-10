from setuptools import find_packages, setup

setup(
    name='coloranalysis',
    packages=find_packages(include=['src/coloranalysis']),
    version='0.1.0',
    description="Retrieves color palette from imgix hosted image, suggests font color",
    author='Kim',
    license='MIT',
)