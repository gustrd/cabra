# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZqHM-Oxl1kfsfJzD3OdWu49EgCfbnT3K
"""
# !pip install libretranslatepy
# Download the dataset
# !wget https://huggingface.co/datasets/databricks/databricks-dolly-15k/resolve/main/databricks-dolly-15k.jsonl

import json
from tqdm import tqdm
from itertools import islice
from libretranslatepy import LibreTranslateAPI

def translate_data(input_file_path, output_file_path, fields_to_translate, libre_translate_url, translate_from, translate_to):

    lt = LibreTranslateAPI(url=libre_translate_url)

    # Count the total number of lines
    with open(input_file_path, 'r') as file:
        total_lines = sum(1 for _ in file)

    print(f"Total number of lines: {total_lines}")

    # Count the total number of already translated lines
    try:
      with open(output_file_path, 'r') as file:
          translated_lines = sum(1 for _ in file)
    except FileNotFoundError:
      print(f"No output file found at {output_file_path}. Assuming no lines have been translated yet.")
      translated_lines = 0
    print(f"Total number of already translated lines: {translated_lines}")

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:

        current_line = translated_lines
        with tqdm(total=total_lines) as loop_controller:
            for j, line in enumerate(islice(input_file, translated_lines, None)):
                current_line += 1

                data = json.loads(line)
                loop_controller.update(1)
                # Translate necessary fields
                for field in fields_to_translate:
                    if field in data and data[field] != "":
                        if isinstance(data[field], list):
                            data[field] = data[field][0]
                        original_text = data[field]
                        translation = lt.translate(original_text, translate_from, translate_to)
                        translation = translation.replace("Inglês","Português")
                        translation = translation.replace("inglês","português")
                        #print(translation)
                        data[field] = translation
                    else:
                        data[field] = ""

                # Save translated entry in the output file
                output_file.write(json.dumps(data) + '\n')

                # Print processed percentage
                percentage = ((current_line + 1) / total_lines) * 100
                print(f'\n-----> Line {current_line}/{total_lines} -----> Processed percentage: {percentage:.2f}\n')

def main():
    # Set the variables
    input_file_path = "./databricks-dolly-15k.jsonl"
    output_file_path = "./output.jsonl"
    fields_to_translate = ['instruction', 'context', 'response'] # Must be adapted to each different dataset
    libre_translate_url = "http://127.0.0.1:5000" # It's better to host a local LibreTranslate server, check their GitHub repo. Or you can subscribe to their service, if you do so you must provide the API Key.
    translate_from='en'
    translate_to='pt'

    # Run
    translate_data(input_file_path, output_file_path, fields_to_translate, libre_translate_url, translate_from, translate_to)

if __name__ == '__main__':
    main()