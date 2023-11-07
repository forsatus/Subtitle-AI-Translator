
# Subtitle-AI-Translator

Subtitle-AI-Translator is an AI-powered application designed to automatically translate video subtitles, making content accessible across different languages and cultures. This tool leverages advanced machine learning models to provide accurate and context-aware translations, ensuring that your video content is enjoyed by a broader audience without language barriers.

## Features

- **Automated Translation**: Quickly translate subtitles from one language to another with support for multiple languages.
- **AI Integration**: Utilizes state-of-the-art AI translation models for high-quality subtitle translation.
- **Customizable**: Easy to tailor the translation process to fit specific needs or preferences.
- **Batch Processing**: Translate entire subtitle files in one go, saving time and effort.
- **User-Friendly**: Designed with simplicity in mind, making it accessible for both technical and non-technical users.

## Installation

There are two main methods to install Subtitle-AI-Translator: using pip, or installing from source. Below are the instructions for both methods.

### Installing with pip

To install Subtitle-AI-Translator using pip, simply run the following command in your terminal:

```
pip install subtitle-ai-translator
```

This will download and install the latest version of Subtitle-AI-Translator along with its dependencies.

### Installing from Source

If you prefer to install from the source, you can clone the repository and install it manually:

```
git clone https://github.com/sutasrof/Subtitle-AI-Translator.git
cd Subtitle-AI-Translator
pip install .
```

This sequence of commands will clone the repository to your local machine, navigate into the project directory, and install the package along with its required dependencies.

## Usage

After installation, you can use Subtitle-AI-Translator from the command line. Here is a basic example of how to use the tool to translate a subtitle file:

```
subtitle_ai_translator source.vtt destination.vtt target_language_code
```

Replace `source.vtt` with the path to your original subtitle file, `destination.vtt` with the path where you want the translated file to be saved, and `target_language_code` with the desired language code (e.g., `en` for English, `es` for Spanish, etc.).
