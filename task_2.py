from task_1 import *
import re
import json
import sys
from typing import Union
import os


def searching_string(target: str,sentences: list[list[str]])-> list[Union[str, int]]:
     # this function searches the string and then returns it in a list
     target_pattern = re.escape(target)
     pattern = r'\b{}\b'.format(target_pattern)
     matches = re.findall(pattern, sentences)
     return [target, len(matches)]


def all_strings(sentences: list[list[str]], n: int)-> list[list[str]]:
    # this functions returns all the strings from all the sizes in the sentences
    try :
        result_list = []
        new_list =[]
        for i in range(n+1):
            temp_list =[]
            for sentence in sentences:
                if len(sentence) >= i :
                #  joined_sentence = " ".join(sentence)
                    temp_list.extend([" ".join(map(str, sentence[j:j + i])) for j in range(len(sentence) - i + 1)])
                # temp_list.extend([" ".join(sentence[j:j + i]) for j in range(len(sentence) - i +1)])
            result_list.append(temp_list)
        for j in range(1,len(result_list)): # removing empty lists
            new_list.append(result_list[j])
        return new_list
    except Exception as e:
        sys.exit("Invalid Input")


def dict_to_list(sentences_dict: dict[str, dict[str,list]])-> Union[list[list[str]], str]:
    # this function extracts the sentences and names from the json file
    result = []
    try :
    # Get the first key and its value
        first_key = next(iter(sentences_dict))  # Get the first key from the dictionary
        value = sentences_dict[first_key]
    # Extract the "Processed Sentences" and "Processed Names" lists
        processed_sentences = value.get('Processed Sentences')
    # Flatten "Processed Sentences" (each sentence as its own list)
        for sentence in processed_sentences:
            result.append(sentence)
        return result
    except Exception as e :
        sys.exit("Invalid Input")

def sequences(sentences: list[list[str]], n: int, string_list:list[list])-> list[list[list[Union[str, int]]]]:
    # this function generated the sequences
    try :
        result_list = []
        seen_words = set()
        for i in range(n):  # Process each subset of `string_list`
            temp_list = []
            for word in string_list[i]:
                new_count = 0
                for sentence in sentences:
                    concatenated_sentence = " ".join(sentence)
                    word, count = searching_string(word, concatenated_sentence)
                    new_count += count
                if word not in seen_words: # add to the seen words to make sure there are no duplicates
                    temp_list.append([word, new_count])
                    seen_words.add(word)
            temp_list.sort(key=lambda x: x[0])  # Sort by word for consistency
            result_list.append(temp_list)
        return result_list
    except Exception as e:
        sys.exit("Invalid Input")


def grouping(sequence: list[list[list[Union[str, int]]]],n: int)->str :
    # this function groups the sequences and returns the json file of the output
    try :
        result = {f"Question 2": {f"{n}-Seq Counts": []}}
        for i in range(1, n + 1):
            # Extract sequences for the current N
            seq_key = f"{i}_seq"
            sequences = sequence[i - 1] if i - 1 < len(sequence) else []

            # Append the formatted group to the result
            result[f"Question 2"][f"{n}-Seq Counts"].append([seq_key, sequences])

            # Convert to a JSON-like string with pretty printing
        return json.dumps(result, indent=4)
    except Exception as e :
        sys.exit("Invalid Input")

def file_type(sentence_input_path: str,people_input_path: str,remove_input_path: str)-> Union[dict[str,dict[str,list]] , str]:
    """ this function returns whether the file that was inserted is a json
     file or csv and acts accordingly"""
    _, names_extension = os.path.splitext(people_input_path)
    _, remove_extension = os.path.splitext(remove_input_path)
    _, file_extension = os.path.splitext(sentence_input_path)
    if file_extension.lower() == ".json":
        try:
            with open(sentence_input_path, 'r') as file:
                data = json.load(file)
            return data  # Return the content of the JSON file
        except Exception as e: # if the file can't be opened
            sys.exit("Invalid Input")

    elif file_extension.lower() == ".csv":
        return initial_text_processing(sentence_input_path,people_input_path,remove_input_path)

    elif names_extension.lower() == ".csv" or remove_extension.lower() == ".csv":
            sys.exit("Invalid Input")
    else : sys.exit("Invalid Input")


