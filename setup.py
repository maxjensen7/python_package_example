from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = 'sample',
    version = '0.0.1',
    description = "A sample Python project",
    long_description = long_description,
    url = "https://github.com/maxjensen7/python_package_example",
    author = "Max Jensen",
    author_email = "max.jensen@inmarsatgov.com",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ]
    
    keywords = "sample, setuptools, development",
    packages = find_packages(where="src"),
    python_requires = ">=3.7, <4",
    install_requires = ["peppercorn"]
)
