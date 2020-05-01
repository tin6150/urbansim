# Install setuptools if not installed.
try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages


# read README as the long description
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='urbansim',
    version='3.1.1',
    description='Tool for modeling metropolitan real estate markets',
    long_description=long_description,
    author='UrbanSim Inc.',
    author_email='info@urbansim.com',
    license='BSD',
    url='https://github.com/udst/urbansim',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License'
    ],
    package_data={
        '': ['*.html'],
    },
    packages=find_packages(exclude=['*.tests']),
    install_requires=[
        'numpy >= 1.8.0',
        'orca >= 1.1',
        'pandas >= 0.17.0',
        'patsy >= 0.3.0',
        'prettytable >= 0.7.2',
        'pyyaml >= 3.10',
        'scipy >= 1.0',
        'statsmodels >= 0.8, <0.11; python_version <"3.6"',
        'statsmodels >= 0.8; python_version >="3.6"',
        'toolz >= 0.8.1'
    ]
)
