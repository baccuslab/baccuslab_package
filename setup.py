from setuptools import setup

setup(
    name='lab_package',
    version='1.0.0',
    description='Template lab package for visprotocol',
    url='https://github.com/ClandininLab/visprotocol',
    author='Max Turner',
    author_email='mhturner@stanford.edu',
    packages=['lab_package'],
    install_requires=[
        'visprotocol',
        ],
    include_package_data=True,
    zip_safe=False,
)
