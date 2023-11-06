"""
This script is designed to translate subtitle files in the VTT (WebVTT) format using AI-powered translation.

Utilizing the M2M100 model from Hugging Face's transformers library, the script is capable of translating subtitle text from the source language to a specified target language. The script supports batch processing to enhance the efficiency of translation by processing multiple subtitle lines simultaneously.

Subtitle lines that contain timestamps or are empty are preserved as is, while subtitle text is translated and reinserted with the appropriate timestamps.

The script is intended to be called from the command line with the following arguments:
- source: the path to the source subtitle file to be translated.
- destination: the path to the subtitle file where the translation should be saved.
- language: the target language code for the translation.

A pre-trained model and tokenizer are used to perform the translation, which are specified within the script. The user has the option to change the model by altering the `model_name` variable.

Usage:
    python script_name.py source.vtt destination.vtt target_language_code

Example:
    python script_name.py subtitles.vtt translated_subtitles.vtt es

The script also includes functions that can be integrated into other Python modules if subtitle translation capabilities are required elsewhere.

Note: This script requires the 'transformers' and 'regex' libraries. Ensure these are installed in your Python environment before running the script.
"""
import argparse
import re
from transformers import AutoTokenizer, M2M100ForConditionalGeneration

# Compile the regex pattern once
timestamp_pattern = re.compile(r'^\d{2}:\d{2}(?::\d{2})?\.\d{3} --> \d{2}:\d{2}(?::\d{2})?\.\d{3}')

def translate_batch(text_batch, dest_lang, model, tokenizer):
    """
    Translates a batch of text into the specified destination language.

    This function takes a list of text strings and the target language code, and uses the provided
    model and tokenizer to generate the translations. The function handles the tokenization of the input text,
    the generation of translated tokens, and the decoding of these tokens back into translated strings.

    Args:
        text_batch (list of str): A list of text strings to be translated.
        dest_lang (str): The target language code to which the text should be translated.
        model (transformers.PreTrainedModel): A pre-trained model from the `transformers` library.
        tokenizer (transformers.PreTrainedTokenizer): A tokenizer that corresponds to the `model`.

    Returns:
        list of str: A list of translated text strings.

    Example:
        >>> model_name = 'facebook/m2m100_418M'
        >>> model = M2M100ForConditionalGeneration.from_pretrained(model_name)
        >>> tokenizer = AutoTokenizer.from_pretrained(model_name)
        >>> text_batch = ["Hello, world!", "How are you?"]
        >>> dest_lang = 'fr'
        >>> translate_batch(text_batch, dest_lang, model, tokenizer)
        ['Bonjour, monde !', 'Comment ça va ?']
    """
    model_inputs = tokenizer(text_batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
    gen_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id(dest_lang))
    translations = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)
    return translations

def extract_and_translate_from_vtt(file_path, output_path, language, model, tokenizer, batch_size=10):
    subtitle_batch = []

    with open(file_path, 'r', encoding='utf-8') as vtt_file, open(output_path, 'w', encoding='utf-8') as out_file:
        for line in vtt_file:
            if timestamp_pattern.match(line.strip()) or line.strip() == "":
                # If we have a batch ready, translate it before writing the timestamp
                if subtitle_batch:
                    translations = translate_batch(subtitle_batch, language, model, tokenizer)
                    for translation in translations:
                        out_file.write(translation + '\n')
                    subtitle_batch = []  # Reset the batch
                out_file.write(line)
            else:
                subtitle_batch.append(line.strip())
                if len(subtitle_batch) == batch_size:
                    translations = translate_batch(subtitle_batch, language, model, tokenizer)
                    for translation in translations:
                        out_file.write(translation + '\n')
                    subtitle_batch = []  # Reset the batch

        # Handle the last batch
        if subtitle_batch:
            translations = translate_batch(subtitle_batch, language, model, tokenizer)
            for translation in translations:
                out_file.write(translation + '\n')

def main():
    parser = argparse.ArgumentParser(description='Translate VTT files using batch processing.')
    parser.add_argument('source', help='The source subtitle file to translate.')
    parser.add_argument('destination', help='The subtitle file where to save the translation.')
    parser.add_argument('language', help='The target language code for the translation.')
    args = parser.parse_args()

    model_name = "facebook/m2m100_418M"
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    extract_and_translate_from_vtt(args.source, args.destination, args.language, model, tokenizer)

if __name__ == "__main__":
    main()
