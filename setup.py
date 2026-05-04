from setuptools import setup, find_packages
from pathlib import Path

__version__: str
exec(Path("molsimple/_version.py").read_text())

setup(
    name="molsimple",
    version=__version__,
    description="",
    keywords="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="DiegoBarMor",
    author_email="diegobarmor42@gmail.com",
    url="https://github.com/diegobarmor/molsimple",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
