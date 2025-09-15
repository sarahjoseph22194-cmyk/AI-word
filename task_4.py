from task_3 import *
import json
import sys


def key_to_search(keys_dict: dict[str,list[list[str]]], remove: str)-> list[list[str]]:
    # this function cleans the keys dict file that's an input
    try:
        if type(keys_dict) == dict:
            processed_names = keys_dict.get('keys', {})
            result_list = []
            seen_words = set()
            for name in processed_names:
                temp_list = []
                for word in name:
                    # Ensure `word` is processed as a single string
                    cleaned_word = string_cleaning(word.strip(), remove).replace(" ", "").strip()  # Pass the word directly to string_cleaning
                    if cleaned_word not in seen_words and cleaned_word != "":  # Add word if it hasn't been seen yet
                        temp_list.append(cleaned_word)
                        seen_words.add(' '.join(cleaned_word))
                result_list.append(temp_list)
            joined_data = [[' '.join(inner_list)] for inner_list in result_list]
            return joined_data
        else : sys.exit("Invalid Input")
    except Exception as e:
        sys.exit("Invalid Input")

def keys_in_sentence(sentences: list[list[str]], keys_list: list[list[str]])-> dict[str,list[list[str]]]:
    """ this function goes over the keys in the cleaned keys list and searches for the sentences in which
    the key is appearing and returns the result of a list of the key and the sentences it appears in it
    """
    try :
        result_dict = {}
        new_sentences = [" ".join(sentence).lower() for sentence in sentences]

        # Iterate over the sorted keys_list
        for key in sorted(keys_list, key=lambda x: " ".join(x).lower()):
            temp_list = []
            key = " ".join(key).lower()
            if key == "":
                continue
            # Search for the key in each sentence
            for sentence in new_sentences:
                _, substring_count = searching_string(key, sentence)
                if substring_count > 0:
                    temp_list.append(sentence.split())
            # Store results in dictionary, with key as the lowercased string
            if temp_list:
                result_dict[key] = sorted(temp_list, key=lambda x: " ".join(x).lower())
        return result_dict
    except  Exception as e:
        sys.exit("Invalid Input")

def grouping_function(keys_dict: dict[str,list[list[str]]])-> str:
    # this function formats the result and returns it in a json file
    try :
        formatted_result = {
            "Question 4": {
                "K-Seq Matches": []
            }
        }

        # Iterate through the result_dict to reformat it
        for key, value in keys_dict.items():
            formatted_result["Question 4"]["K-Seq Matches"].append([key, value])
        return json.dumps(formatted_result, indent=4)
    except  Exception as e:
        sys.exit("Invalid Input")

def json_file_opening(file_path: str)-> any:
    # this function opens the json file and returns its content
    try :
        with open(file_path, 'r') as file:
            content = json.load(file)  # Parse JSON content into a Python object
        return content
    except Exception as e:
        sys.exit("Invalid Input")
