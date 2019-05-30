from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name='kbpybot',
    version='0.0.1',
    description='python bot client for keybase',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author=['keybase developers'],
    install_requires=['mashumaro'],
    author_email='alex@keyba.se'
)
