from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="timein",
    version="0.2",
    packages=["timein"],
    install_requires=["requests"],
    python_requires='>=3.5',
    description="Shell gadget to return the time in a city",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Steve Nixon",
    author_email="snixon@gmail.com",
    url="https://www.beer-fueled.dev",
    platforms=["Any"],
    entry_points={
        "console_scripts": ["timein = timein.main:main"]
    },
)
