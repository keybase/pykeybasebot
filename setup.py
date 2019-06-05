from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='pykeybasebot',
    version='0.1.0',
    description='python bot client for keybase',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/keybase/pykeybasebot',
    license=license,
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author=['keybase developers'],
    install_requires=['mashumaro==1.6.2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author_email='alex@keyba.se',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications :: Chat :: Keybase',
        'Framework :: Robot Framework :: Library',
        'Framework :: Robot Framework :: Tool',
        'Keybase',
    ]
)
