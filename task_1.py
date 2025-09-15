# this file is just for Task 1
from typing import Union, LiteralString
import re
import json
import csv
import sys


def read_csv_file(csv_path: str) -> Union[list, str]:
    """Reads a CSV file and returns its content as a list of lists or strings."""
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader if any(cell.strip() for cell in row)]  # Skip empty rows
    except FileNotFoundError:
        sys.exit("Invalid Input")
    except Exception as e:
        sys.exit(f"Invalid Input")


def sentence_breaking(sentence_input_path: str) -> list:
    """ This function does all the cleaning of the  sentences file that's given , it removes the whitespace,
    punctuation. splits the words/sentences into lists
    """
    sentence=read_csv_file(sentence_input_path)
    sentences_cleaned = []
    for sentence_list in sentence:
        # For each sentence, join it into a single string, remove punctuation, and split into words

        sentence_text = ' '.join(sentence_list)
        sentence_text = re.sub(r"'*\b", " *", sentence_text)
        sentence_text = re.sub(r"[—-]+", " ", sentence_text)
        sentence_text = re.sub(r"[,\/*\+=()&^%.$#@!~`':;?><{-}[\]]", "", sentence_text)  # Remove punctuation
        sentence_text = re.sub(r'\s+', ' ', sentence_text).strip()  # Normalize spaces
        words = sentence_text.lower().split()  # Convert to lowercase and split into words

        sentences_cleaned.append(words)  # Append the cleaned sentence (as a list of words)

    return sentences_cleaned

def dictionary_of_names(name_input_path: str, remove: str) -> dict[str, list[str]]:
    try :
        names = read_csv_file(name_input_path)
        removed = read_csv_file(remove)

        # Flatten and normalize `removed` to a list of lowercase strings
        flattened_removed = [item.strip().lower() for sublist in removed for item in sublist]
        result_dict = {}
        if names == []:
            return {}
        for i in range(1, len(names)):  # Start from 1 to skip headers
            temp_list = []
            for j in range(1, len(names[i])):  # Iterate through the names column
                for phrase in names[i][j].split(','):
                    phrase = phrase.strip().lower()  # Normalize the phrase
                    if phrase not in flattened_removed:  # Check if not in removed list
                        temp_list.append(phrase.strip())

            result_dict[names[i][0]] = temp_list  # Update the dictionary with cleaned names
        return result_dict
    except  Exception as e:
        sys.exit("Invalid Input")


def string_cleaning(word: str, remove: str) -> str:
    # Ensure the 'remove' list is flattened and normalized
    flattened_removed = [item.strip().lower() for sublist in remove for item in
                         (sublist if isinstance(sublist, list) else [sublist])]

    # Convert word to lowercase and strip whitespace
    word = word.lower().strip()

    # Handle possessive cases and replace hyphens
    word = word.replace("'", "").replace("-", " ")

    # Apply regex cleaning to remove special characters
    word = re.sub(r"[,\/*\+-=()&^%.$#@!~`.':;?><{.}\[\]]", " ", word)
    word = re.sub(r'\s+', ' ', word).strip()  # Normalize whitespace

    # Split the word into tokens (split by spaces after processing hyphens)
    tokens = word.split()

    # Remove unwanted words and single-character words
    cleaned_word = " ".join(
        [w for w in tokens if w not in flattened_removed and len(w) > 1]
    )

    return cleaned_word

def dictionary_cleaning(names_dict: dict, remove: str) -> dict:
    # Ensure the 'remove' list is flattened and normalized
    try :
        removed = [item.strip().lower() for sublist in read_csv_file(remove) for item in
               (sublist if isinstance(sublist, list) else [sublist])]

        new_dict = {}
        if not names_dict:
            return {}

        for key, value in names_dict.items():
        # Debug: Check the original key and value

        # Clean the key
            cleaned_key_parts = [
            string_cleaning(word, removed)
                for word in re.split(r"[ -']", key)
                if string_cleaning(word, removed)
            ]
            cleaned_key = " ".join(cleaned_key_parts).strip()

            # Clean the values (descriptions)
            cleaned_value = []
            for item in value:
                cleaned_value_parts = [
                    string_cleaning(word, removed)
                    for word in item.split()
                    if string_cleaning(word, removed)
                ]
                cleaned_value.append(" ".join(cleaned_value_parts).strip())

            # Debug: Check the cleaned key and value

            # Add the cleaned key-value pair to the new dictionary
            if cleaned_key:
                new_dict[cleaned_key] = cleaned_value
        return new_dict
    except  Exception as e:
        sys.exit("Invalid Input")



def grouping_names(dictionary: dict) -> list:
    try :
        result_list = []
        if dictionary == {} :
            return [[[]]]
        for key, values in dictionary.items():
            # Split the key into individual words
            key_structure = [key.split() ]

            # Process values: Split each value into words, filter out empty or unwanted values
            cleaned_values = [value.split() for value in values if value and value != "\""]

            # Add cleaned values or an empty list
            if cleaned_values:
                key_structure.append(cleaned_values)
            else:
                key_structure.append([])  # Avoid additional nested lists

            result_list.append(key_structure)
        return result_list
    except  Exception as e:
        sys.exit("Invalid Input")



def sentence_output(remove_words: list[str], sentence_input_path: str)-> list:
    try:
        """ this function double checks that there are no remove words
        as well as doesn't add empty words or set of parenthesis to the result list """
        remove_words_set = list(word[0] for word in remove_words if word)
        sentences = sentence_breaking(sentence_input_path)
        for i in range(len(sentences)):
            sentences[i]= [word for word in sentences[i] if word not in remove_words_set]
        new_sentence =[]
        for j in range(1,len(sentences)):
            if (sentences[j]) != [] :
                new_sentence.append(sentences[j])
        return new_sentence
    except Exception as e:
        sys.exit(f"Invalid Input")


def initial_text_processing(sentence_input_path: str,people_input_path: str,remove_input_path: str) -> dict[str,dict[str,list]]:
    # task number 1
    args = {'question_number': 1}
    remove = read_csv_file(remove_input_path)
    # cleaning and presenting the words in the sentences
    sentences=sentence_output(remove ,sentence_input_path)
    # cleaning the words file
    dict = dictionary_cleaning(dictionary_of_names(people_input_path, remove_input_path), remove_input_path)
    names = grouping_names(dict)
    output = {
        f"Question {args['question_number']}": {
        "Processed Sentences": sentences ,
        "Processed Names": names
    }}
    json_file_path = 'output.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(output, json_file, indent=4)

    return output

