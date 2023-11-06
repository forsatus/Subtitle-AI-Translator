from setuptools import setup, find_packages

setup(
    name='subtitle-ai-translator',
    version='1.0',
    packages=find_packages(),
    description='AI-powered tool for seamless subtitle translation, enabling cross-language accessibility for video content.',
    long_description=open('README.md', encoding='utf-8').read(),
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
