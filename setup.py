from setuptools import setup

setup(
	version='0.1',
    name='mimicrnn',
    author='Jordan Coblin',
    packages=['mimicrnn'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)