import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AIM-Sanyn", # Replace with your own username
    version="0.1.0",
    author="Zsombor Papp",
    author_email="pzsombor2002@gmail.com",
    description="AIM is a python library, that can handle (almost) infinitely big or small numbers. It was devloped for the Papp algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sanyn/AIM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)