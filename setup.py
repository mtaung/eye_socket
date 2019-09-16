import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pupil_socket",
    version = "0.0.1",
    author = "Myat Aung",
    author_email = "mta510@york.ac.uk",
    description = ("Simple ZMQ socket to communicate with pupil-recorder."),
    license = "MIT",
    keywords = "pupil-labs psychopy",
    url = "https://github.com/mtaung/pupil_socket",
    packages=['pupil_socket'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: Testing-Alpha",
        "Topic :: Utilities",
        "License :: MIT License",
    ],
)