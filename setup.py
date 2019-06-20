from distutils.core import setup
from setuptools import find_packages
from statsdb import __version__

setup(
    name='statsdb-python',
    version=__version__,
    description='',
    url='http://github.com/Public-Health-Bioinformatics/statsdb-python',
    author='',
    author_email='',
    license='GPLv3',
    packages=['statsdb'],
    include_package_data=True,
    keywords = "",
    project_urls = {
        "Bug Reports": "https://github.com/Public-Health-Bioinformatics/statsdb-python/issues",
        "Change Log":  "https://github.com/Public-Health-Bioinformatics/statsdb-python/CHANGES.md",
        "Source":      "https://github.com/Public-Health-Bioinformatics/statsdb-python",
    },
    scripts=[
    ],
    zip_safe=False,
    python_requires = '>=3.4',
    install_requires = [
        "mysqlclient",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GPLv3 License",  
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        
    ],
)
