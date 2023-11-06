import argparse
import re
from transformers import AutoTokenizer, M2M100ForConditionalGeneration

# Compile the regex pattern once
timestamp_pattern = re.compile(r'^\d{2}:\d{2}(?::\d{2})?\.\d{3} --> \d{2}:\d{2}(?::\d{2})?\.\d{3}')

def translate_batch(text_batch, dest_lang, model, tokenizer):
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
