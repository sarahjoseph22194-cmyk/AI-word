from unittest import result

from task_3 import *
import sys
def flatten_list(nested_list: list[str])->list[str]:
    """Flatten a list of lists into a single list."""
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  # Recursively flatten the list
        else:
            flattened.append(item)
    return flattened

def key_in_sentence(sentences:list[list[str]], key:list[str]) -> dict[str,list[list[str]]]:
    """
    Checks if a key (name or phrase) is present in any of the sentences.

    - If the key is a compound name (e.g., "albus dumbledore"), checks each part (e.g., "albus" or "dumbledore").
    - If the key is a single phrase (e.g., "undesirable one"), checks for the whole phrase.
    """
    try :
        result_dict = {}

        # Ensure key is a string or a flattened, normalized string
        if isinstance(key, list):
            key = " ".join(flatten_list(key)).strip()
        key_normalized = key.lower()
        key_parts = key_normalized.split()  # Split into individual parts for compound names
        # Normalize sentences
        sentences_normalized = [" ".join(sentence).lower() for sentence in sentences]

        matching_sentences = []

        for sentence, sentence_text in zip(sentences, sentences_normalized):
        # For compound names, check individual parts

            if all(part in sentence_text for part in key_parts):
                matching_sentences.append(sentence)

            else:  # For single names or phrases, check the full string
                if key_normalized in sentence_text:
                    matching_sentences.append(sentence)

        if matching_sentences:
            result_dict[key] = matching_sentences
        return result_dict
    except  Exception as e:
        sys.exit("Invalid Input")

def all_sentences(sentences: list[list[str]], names_list: list[list[str]])-> dict[str,list[list[str]]] :
    """
    Matches names or phrases in names_list with sentences and returns a dictionary.
    """
    try :
        def key_in_sentence_compound(sentences: list[list[str]], key: str)-> list[list[str]]:
            """
            Handles compound names by breaking the first name into parts and looking for full matches for the rest.
            """
            key_normalized = key.lower()
            key_parts = key_normalized.split()
            matching_sentences = []

            # Normalize sentences
            sentences_normalized = [" ".join(sentence).lower() for sentence in sentences]

            for sentence, sentence_text in zip(sentences, sentences_normalized):
                # Check if any part of the name is in the sentence
                if all(part in sentence_text for part in key_parts): # checking if all the key is in the sentence
                    matching_sentences.append(sentence)

            return matching_sentences

        result_dict = {}

        for name_group in names_list:
            # Flatten nested lists and normalize names
            flat_names = [
                " ".join(name).strip() if isinstance(name, list) else name.strip()
                for name in name_group if name
            ]

            # Skip empty name groups
            if not flat_names:
                continue

            combined_sentences = set()  # Use a set to avoid duplicate sentences

            # Process the first name separately
            if flat_names:
                first_name = flat_names[0]
                names = first_name.split()
                for word in names: # searching the components of the first name
                    matching_sentences = key_in_sentence_compound(sentences, word)
                    # print(word,matching_sentences)
                    combined_sentences.update(tuple(sentence) for sentence in matching_sentences)

                # Process remaining names as whole strings
                for name in flat_names[1:]:  # in case there are other names
                    temp_sentences = key_in_sentence(sentences, name)
                    for sentence_list in temp_sentences.values():
                        combined_sentences.update(tuple(sentence) for sentence in sentence_list)

            # Assign the combined sentences (converted back to lists) to the first valid name in the group
            if combined_sentences:
                result_dict[flat_names[0]] = sorted(
                    [list(sentence) for sentence in combined_sentences],
                    key=lambda x: " ".join(x).lower()
                )
            else:
                result_dict[flat_names[0]] = []  # Add empty list if no matches found

        return result_dict
    except  Exception as e:
        sys.exit("Invalid Input")

def extract_k_sequences_flat(data: dict[str,list[list[str]]], n: int)-> list[list[str| list[list]]]:
    """
    Extracts k-sequences from the input data and returns them in the specified flattened format.

    Parameters:
    - data: Dictionary where keys are persons and values are lists of sentences (each sentence as a list of words).
    - N: Maximum k-sequence length to extract.

    Returns:
    - A list containing each person's name and their k-sequences as nested lists of words.
    """
    try :
        result = []

        for person, sentences in data.items():
            sequences = set()  # Use a set to avoid duplicate sequences

            # Process each sentence to extract k-sequences
            for sentence in sentences:
                flattened_sentence = [word.lower() for word in flatten_list(sentence)]
                for k in range(1, n + 1):
                    sequences = set(sequences)
                    sequences.update(
                        tuple(flattened_sentence[i:i + k]) for i in range(len(flattened_sentence) - k + 1)
                    )
                    sequences = list(sequences)
            # Convert sequences to sorted nested lists
            sorted_sequences = sorted(sequences)  # Sort alphabetically
            formatted_sequences = [list(seq) for seq in sorted_sequences]
            # Add person's name and their sequences to the result
            if formatted_sequences:
                result.append([person, formatted_sequences])
        return result
    except  Exception as e:
        sys.exit("Invalid Input")


def format_as_json(result: list[list[str,list]])-> str:
    """
    Formats the result into the desired JSON structure.

    Parameters:
    - result: A list of lists where each inner list contains a person's name and their k-sequences.

    Returns:
    - A JSON-formatted dictionary.
    """
    try :
        formatted = {
            "Question 5": {
                "Person Contexts and K-Seqs": result
            }
        }
        return json.dumps(formatted, indent=4)
    except Exception as e:
        sys.exit("Invalid Input")

