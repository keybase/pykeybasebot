from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name='pykeybasebot',
    version='0.1.1',
    description='Officially supported Keybase python bot client library',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/keybase/pykeybasebot',
    license='BSD (3 clause)',
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author='Keybase Engineering Team',
    install_requires=['mashumaro==1.6.2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    author_email='alex@keyba.se',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Framework :: Robot Framework :: Library',
        'Framework :: Robot Framework :: Tool',
    ]
)
