import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winbackground-HaeckelK",
    version="0.0.2",
    author="HaeckelK",
    author_email="author@example.com",
    description="Basic functions to change windows background",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HaeckelK/winbackground_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
