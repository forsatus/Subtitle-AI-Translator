"""
Setup script for the Subtitle-AI-Translator package.

This script uses setuptools to package the Subtitle-AI-Translator project, 
making it easier to distribute and install. The package is an AI-powered tool 
that provides seamless subtitle translation to enable cross-language 
accessibility for video content.

When this script is run, it will package the project according to the 
configurations specified in the `setup()` function. This includes metadata 
about the project such as its name, version, description, and more.

The packaged project can then be uploaded to PyPI or installed directly 
using pip. The script specifies the package's dependencies, which will be 
automatically installed when the package is installed. It also defines entry 
points for any command-line scripts included in the package.

Package:
    Subtitle-AI-Translator

Version:
    1.0

Author:
    sutasrof (mario.chauvet@icloud.com)

Repository:
    https://github.com/sutasrof/Subtitle-AI-Translator

Requirements:
    Python 3.6 and above

Usage:
    The `setup.py` script should be run using Python's setuptools module:
        `python setup.py sdist bdist_wheel`
    This will generate distribution packages in the `dist` directory.

    The package can then be installed using pip:
        `pip install .`
    This will install the package along with its dependencies.
"""
from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='subtitle-ai-translator',
    version='1.0',
    packages=find_packages(),
    description=('AI-powered tool for seamless subtitle translation, enabling '
                 'cross-language accessibility for video content.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='sutasrof',
    author_email='mario.chauvet@icloud.com',
    url='https://github.com/sutasrof/Subtitle-AI-Translator',
    install_requires=[
        'transformers[torch]>=4.34.1',
        'sentencepiece>=0.1.99'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'subtitle_ai_translator=subtitle_ai_translator.main:main',
        ],
    },
)
