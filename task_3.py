from task_2 import *
import json

def process_data_from_dict(input_dict: dict[str,dict[str,list]])-> list[list[str]]:
    try :
        # this function processes the names that comes out of the output file from task 1
        processed_names = input_dict.get('Question 1', {}).get('Processed Names', [])
        result = []
        for entry in processed_names:
        #  If the second element of the entry is non-empty, process it
            flattened_entry = [" ".join(entry[0])]  # Combine first list into a single phrase
            flattened_entry.extend([" ".join(item) for item in entry[1]])  # Flatten and join sublist
            result.append(flattened_entry)
        result.sort(key=lambda x: x[0].lower())
        return result
    except  Exception as e:
        sys.exit("Invalid Input")


def number_of_counters(names_list: list[list[str]], sentences: list[list[str]])-> list[list[Union[str,int]]]:
    """ this function counts the number of occurrences of the name in the sentences
    and only returns the names with a count that's greater than zero
    """
    try :
        seen_words = set()
        result_list = []

        # Preprocess sentences into lowercase strings
        new_sentences = [" ".join(sentence).lower() for sentence in sentences]

        for name_group in names_list:

            total_count = 0
            full_name = name_group[0].lower()
            # Generate all consecutive combinations (substrings) from the name
            substrings = generate_consecutive_substrings(full_name)
            for substring in substrings:
                count = 0
                for sentence in new_sentences:
                    _, substring_count = searching_string(substring, sentence)
                    count += substring_count
                total_count += count
            for name in name_group[1:]:
                new_count = 0
                for sentence in new_sentences:
                    _, substring_count = searching_string(name, sentence)
                    new_count += substring_count
                    total_count += new_count


        # Add to result if not already seen and if the total count > 0
            if total_count > 0:
                result_list.append([name_group[0].lower(), total_count])
                seen_words.add(name_group[0].lower())
        return result_list
    except  Exception as e:
        sys.exit("Invalid Input")

def generate_consecutive_substrings(name: str)-> list[str]:
    # this function breaks the name into substrings
    words = name.split()
    substrings = []
    for start in range(len(words)):
        for end in range(start + 1, len(words) + 1):
            substrings.append(" ".join(words[start:end]))
    return substrings

def grouping_func(names_occurrences: list[list[Union[str,int]]])-> str:
    # this function prints the output as a json file
    output = {
        "Question 3": {
            "Name Mentions": names_occurrences
        }
    }
    return json.dumps(output, indent=4)

