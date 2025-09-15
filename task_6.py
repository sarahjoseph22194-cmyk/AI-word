from task_3 import *
def matching_pair(person_one: str, person_two: str, sentences:list[list[str]], k: int)-> int:
    # this function returns the count of many times did person one and person two appeared in the sentences
    count = 0

    # Tokenize the names into individual words
    person_one_words = set(person_one.split())
    person_two_words = set(person_two.split())

    # Iterate through the list of sentences with a sliding window of size k
    for i in range(len(sentences) - k + 1):
        # Flatten the sentences in the current window into a single list of words
        window_words = [word for sentence in sentences[i:i + k] for word in sentence]

        # Check if there's at least one word from person_one and one word from person_two in the window
        if any(word in window_words for word in person_one_words) and \
                any(word in window_words for word in person_two_words):
            count += 1  # Increment count if both person_one and person_two words are in the window

    return count

def pairs_occurrences(sentences: list[list[str]], names_list:list[list[str]], k: int)-> dict[tuple[str,str],int]:
    ''' this function returns a dictionary of the names of the people and how many times
     did they appear in the sentences (together)
    '''
    result_dict = {}

    # Iterate through all unique pairs of names
    for i in range(len(names_list)):
        for j in range(i + 1, len(names_list)):
            person_one_list = names_list[i]
            person_two_list = names_list[j]

            # Extract the primary name from each list
            person_one_primary = person_one_list[0]
            person_two_primary = person_two_list[0]

            # Flatten lists of names to handle cases where multiple names are present
            for person_one in person_one_list:
                for person_two in person_two_list:
                    # We only count for the primary names
                    if person_one == person_one_primary and person_two == person_two_primary:
                        count = matching_pair(person_one, person_two, sentences, k)

                        # Store results in the dictionary
                        if (person_one, person_two) not in result_dict:
                            result_dict[(person_one, person_two)] = count
                        # If we already counted this pair, add the count together
                        else:
                            result_dict[(person_one, person_two)] += count

    return result_dict

def format_result_to_json(pair_counts: dict[tuple[str,str],int], threshold: int) -> str:
    # Extract pairs with counts greater than the threshold
    filtered_pairs = [[person.split() for person in pair] for pair, count in pair_counts.items() if count >= threshold]

    # Create the result in the required JSON format
    output = {
        "Question 6": {
            "Pair Matches": filtered_pairs
        }
    }

    # Convert the result to a JSON string (for printing or saving to a file)
    return json.dumps(output, indent=4)

