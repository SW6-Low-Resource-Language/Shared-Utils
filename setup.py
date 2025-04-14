from setuptools import setup, find_packages

setup(
    name='shared-resources',
    version='0.1.0',
    author='Lasse Drongesen',
    author_email='Lassemgp@gmail.com',
    description='A collection of shared utilities for the repositories',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here, for example:
        # 'somepackage>=1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)