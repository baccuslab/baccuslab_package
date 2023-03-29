from setuptools import setup

setup(
    name='lab_package',
    version='3.0.0',
    description='Template lab package for visprotocol',
    url='https://github.com/mhturner/lab_package',
    author='Max Turner',
    author_email='mhturner@stanford.edu',
    packages=['lab_protocol'],
    include_package_data=True,
    zip_safe=False,
)
