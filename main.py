#!/usr/bin/env python3

import argparse
import sys
from email.utils import parsedate_to_datetime
from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
from task_5 import *
from task_6 import *
from task_7 import *
from task_8 import *
from task_9 import *
def readargs(args=None):
    try :
        parser = argparse.ArgumentParser(
        prog='Text Analyzer project',
        )
        # General arguments
        parser.add_argument('-t', '--task',
                        help="task number", type=int,
                        required=True
                        )
        parser.add_argument('-s', '--sentences',
                        help="Sentence file path",
                        )
        parser.add_argument('-n', '--names',
                        help="Names file path",
                        )
        parser.add_argument('-r', '--removewords',
                        help="Words to remove file path",
                        )
        parser.add_argument('-p', '--preprocessed',
                        action='append',
                        help="json with preprocessed data",
                        )
        # Task specific arguments
        parser.add_argument('--maxk',
                        type=int,
                        help="Max k",
                        )
        parser.add_argument('--fixed_length',
                        type=int,
                        help="fixed length to find",
                        )
        parser.add_argument('--windowsize',
                        type=int,
                        help="Window size",
                        )
        parser.add_argument('--pairs',
                        help="json file with list of pairs",
                        )
        parser.add_argument('--threshold',
                        type=int,
                        help="graph connection threshold",
                        )
        parser.add_argument('--maximal_distance',
                        type=int,
                        help="maximal distance between nodes in graph",
                        )

        parser.add_argument('--qsek_query_path',
                        help="json file with query path",
                        )
        return parser
    except Exception as e :
        sys.exit("Invalid Input")

def is_valid_csv(file_path):
    """
    Check if a file is a valid CSV file and can be opened.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a valid CSV and can be opened, False otherwise.
    """
    # Check if the file has a .csv extension
    if not file_path.lower().endswith('.csv'):
        return False

    # Check if the file exists and is readable
    if not os.path.isfile(file_path):
        return False

    try:
        # Attempt to open the file and parse it as a CSV
        with open(file_path, 'r') as file:
            csv.reader(file)
        return True
    except (OSError, csv.Error):
        return False

def is_valid_json(file_path):
    """
    Check if a file is a valid JSON file and can be opened.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a valid JSON and can be opened, False otherwise.
    """
    # Check if the file has a .json extension
    if not file_path.lower().endswith('.json'):
        return False

    # Check if the file exists and is readable
    if not os.path.isfile(file_path):
        return False

    try:
        # Attempt to open the file and parse it as JSON
        with open(file_path, 'r') as file:
            json.load(file)
        return True
    except (OSError, json.JSONDecodeError):
        return False

def valid_args(parsed_args):
    if parsed_args["sentences"] and not is_valid_csv(parsed_args["sentences"]):
        sys.exit("Invalid Input")
    if parsed_args["names"] and not is_valid_csv(parsed_args["names"]):
        sys.exit("Invalid Input")
    if parsed_args["removewords"] and not is_valid_csv(parsed_args["removewords"]):
        sys.exit("Invalid Input")
    if parsed_args["preprocessed"] :
        if isinstance(parsed_args["preprocessed"], list):
            if len(parsed_args["preprocessed"]) == 1:
                parsed_args["preprocessed"] = parsed_args["preprocessed"][0]
                if not is_valid_json(parsed_args["preprocessed"]):
                    sys.exit("Invalid Input")
            else : sys.exit("Invalid Input")
        elif isinstance(parsed_args["preprocessed"], str) and not is_valid_json(parsed_args["preprocessed"]) :
            sys.exit("Invalid Input")
    if parsed_args["maxk"] is not None and parsed_args["maxk"] < 0:
        sys.exit("Invalid Input")
    if parsed_args["windowsize"] and parsed_args["windowsize"] < 0 :
        sys.exit("Invalid Input")
    if parsed_args["pairs"]:
        if isinstance(parsed_args["pairs"], list):
            if len(parsed_args["pairs"]) == 1:
                parsed_args["pairs"] = parsed_args["pairs"][0]
                if not is_valid_json(parsed_args["pairs"]):
                    sys.exit("Invalid Input")
            else : sys.exit("Invalid Input")
        elif isinstance(parsed_args["pairs"], str) and not is_valid_json(parsed_args["pairs"]) :
            sys.exit("Invalid Input")

    if parsed_args["threshold"] and parsed_args["threshold"] < 0 :
        sys.exit("Invalid Input")
    if parsed_args["maximal_distance"] and parsed_args["maximal_distance"] < 0 :
        sys.exit("Invalid Input")
    if parsed_args["qsek_query_path"] :
        if isinstance(parsed_args["qsek_query_path"], list):
            if len(parsed_args["qsek_query_path"]) == 1:
                parsed_args["qsek_query_path"] = parsed_args["qsek_query_path"][0]
                if not is_valid_json(parsed_args["qsek_query_path"]):
                    sys.exit("Invalid Input")
            elif isinstance(parsed_args["qsek_query_path"], str) and not is_valid_json(parsed_args["qsek_query_path"]):
                sys.exit("Invalid Input")
    if parsed_args["task"] and( parsed_args["task"] < 1 or  parsed_args["task"] > 9 ):
        sys.exit("Invalid Input")
    if parsed_args["fixed_length"] and parsed_args["fixed_length"] < 0 :
        sys.exit("Invalid Input")
# Generic file opener
def open_file(filepath):
    try:
        with open(filepath, 'r') as file:
            # Try to parse as JSON
            if filepath.endswith('.json'):
                return json.load(file)  # Parse JSON content
            else:
                return file.read()  # Return raw text content for other files
    except FileNotFoundError:
        sys.exit(f"Invalid Input")
    except json.JSONDecodeError:
        sys.exit(f"Invalid Input")
    except Exception as e:
        sys.exit(f"Invalid Input")

def functions_calling(parsed_args):
    try:
        match parsed_args["task"]:
            case 1 :
                try:
                    print(initial_text_processing(parsed_args["sentences"],parsed_args["names"],parsed_args["removewords"]))
                except Exception as e:
                    sys.exit("Invalid Input")
            case 2 :
                if parsed_args["preprocessed"] and parsed_args["maxk"] >= 0 :
                    k = parsed_args["maxk"]
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    sentences_list = dict_to_list(dictionary)
                    strings = all_strings(sentences_list, k)
                    sequence = sequences(sentences_list, k, strings)
                    print(grouping(sequence,k))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["maxk"] >= 0 :
                    dictionary =initial_text_processing(parsed_args["sentences"],parsed_args["names"],parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    strings = all_strings(sentences_list, parsed_args["maxk"])
                    sequence = sequences(sentences_list, parsed_args["maxk"], strings)
                    print(grouping(sequence, parsed_args["maxk"]))
                elif parsed_args["sentences"] and parsed_args["removewords"] and parsed_args["maxk"] >= 0:
                    with open("names_file.csv", "w") as names_file:
                        pass
                    file_path = os.path.abspath("names_file.csv")
                    dictionary = initial_text_processing(parsed_args["sentences"], file_path, parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    strings = all_strings(sentences_list, parsed_args["maxk"])
                    sequence = sequences(sentences_list, parsed_args["maxk"], strings)
                    print(grouping(sequence, parsed_args["maxk"]))
                else :
                    sys.exit("Invalid Input")
            case 3 :
                if parsed_args["preprocessed"]:
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    sentences_list = dict_to_list(dictionary)
                    names_list = process_data_from_dict(dictionary)
                    num = number_of_counters(names_list, sentences_list)
                    print(grouping_func(num))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] :
                    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    names_list = process_data_from_dict(dictionary)
                    num = number_of_counters(names_list, sentences_list)
                    print(grouping_func(num))
                else :
                    sys.exit("Invalid Input")
            case 4 :
                if parsed_args["preprocessed"] and parsed_args["qsek_query_path"] and parsed_args["removewords"]:
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    sentences_list = dict_to_list(dictionary)
                    key_list = json_file_opening(parsed_args["qsek_query_path"])
                    key_list = key_to_search(key_list, parsed_args["removewords"])
                    result = keys_in_sentence(sentences_list, key_list)
                    print(grouping_function(result))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["qsek_query_path"] :
                    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    key_list = json_file_opening(parsed_args["qsek_query_path"])
                    key_list = key_to_search(key_list, parsed_args["removewords"])
                    result = keys_in_sentence(sentences_list, key_list)
                    print(grouping_function(result))
                elif parsed_args["sentences"] and parsed_args["removewords"] and parsed_args["qsek_query_path"] :
                    with open("names_file.csv", "w") as names_file:
                        pass
                    file_path = os.path.abspath("names_file.csv")
                    dictionary = initial_text_processing(parsed_args["sentences"], file_path, parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    key_list = json_file_opening(parsed_args["qsek_query_path"])
                    key_list = key_to_search(key_list, parsed_args["removewords"])
                    result = keys_in_sentence(sentences_list, key_list)
                    print(grouping_function(result))
                else : sys.exit("Invalid Input")
            case 5 :
                if parsed_args["preprocessed"] and isinstance(parsed_args["maxk"], int) and parsed_args["maxk"] >= 0:
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    names_list = process_data_from_dict(dictionary)
                    sentences_list = dict_to_list(dictionary)
                    result = all_sentences(sentences_list, names_list)
                    data = extract_k_sequences_flat(result, parsed_args["maxk"])
                    print(format_as_json(data))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["maxk"] >= 0:
                    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"],parsed_args["removewords"])
                    names_list = process_data_from_dict(dictionary)
                    sentences_list = dict_to_list(dictionary)
                    result = all_sentences(sentences_list, names_list)
                    data = extract_k_sequences_flat(result, parsed_args["maxk"])
                    print(format_as_json(data))
                else : sys.exit("Invalid Input")
            case 6 :
                if parsed_args["preprocessed"] and parsed_args["threshold"] >=0  and parsed_args["windowsize"] > 0  :
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    names_list = process_data_from_dict(dictionary)
                    sentences_list = dict_to_list(dictionary)
                    if parsed_args["windowsize"] <= len(sentences_list) :
                        pairs = pairs_occurrences(sentences_list, names_list, parsed_args["windowsize"])
                        print(format_result_to_json(pairs, parsed_args["threshold"]))
                    else : sys.exit("Invalid Input")
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["windowsize"] >0 and parsed_args["threshold"] >=0 :
                    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
                    names_list = process_data_from_dict(dictionary)
                    sentences_list = dict_to_list(dictionary)
                    if parsed_args["windowsize"] <= len(sentences_list):
                        pairs = pairs_occurrences(sentences_list, names_list, parsed_args["windowsize"])
                        print(format_result_to_json(pairs, parsed_args["threshold"]))
                    else:
                        sys.exit("Invalid Input")
                elif parsed_args["preprocessed"] and parsed_args["threshold"] and parsed_args["windowsize"] == 0 :
                    print(format_result_to_json({}, parsed_args["threshold"]))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args[
                    "windowsize"] == 0 and parsed_args["threshold"]:
                    print(format_result_to_json({}, parsed_args["threshold"]))
                else : sys.exit("Invalid Input")

            case 7 :
                if parsed_args["preprocessed"] and parsed_args["pairs"] and parsed_args["maximal_distance"] >=0 :
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    keys_list = open_file(parsed_args["pairs"])
                    processed_names = dict_processing(dictionary)
                    result_list = checking_connection(keys_list, processed_names,parsed_args["maximal_distance"])
                    print(json_format(result_list))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["pairs"] and parsed_args["maximal_distance"]>=0 and parsed_args["windowsize"]>0  and parsed_args["threshold"]>=0 :
                    dictionary = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    names_list = process_data_from_dict(dictionary)
                    if parsed_args["windowsize"] <= len(sentences_list):
                        pairs = pairs_occurrences(sentences_list, names_list, parsed_args["windowsize"])
                        task_6_output = format_result_to_json(pairs, parsed_args["threshold"])
                        keys_list = open_file(parsed_args["pairs"])
                        processed_names = dict_processing(task_6_output)
                        result_list = checking_connection(keys_list, processed_names,parsed_args["maximal_distance"])
                        print(json_format(result_list))
                    else: sys.exit("Invalid Input")
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["pairs"] and parsed_args["maximal_distance"]>=0 and parsed_args["windowsize"]==0  and parsed_args["threshold"]>=0:
                    print(json_format([]))
                else : sys.exit("Invalid Input")
            case 8 :
                if parsed_args["preprocessed"] and parsed_args["qsek_query_path"] and parsed_args["fixed_length"] >=0:
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    keys = json_file_opening(parsed_args["qsek_query_path"])
                    joined_pairs = dict_processing(dictionary)
                    adj_list = making_adjacency_list(joined_pairs)
                    graph = Graph(adj_list)
                    result = graph.all_the_connections(keys,parsed_args["fixed_length"])
                    print(graph.generate_result_file(result))
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["qsek_query_path"] and parsed_args["fixed_length"] >= 0 and parsed_args["windowsize"] >0 and parsed_args["threshold"]>= 0  :
                    dict = initial_text_processing(parsed_args["sentences"], parsed_args["names"],parsed_args["removewords"])
                    keys = json_file_opening(parsed_args["qsek_query_path"])
                    sentences_list = dict_to_list(dict)
                    names_list = process_data_from_dict(dict)
                    if parsed_args["windowsize"] <= len(sentences_list):
                        pairs = pairs_occurrences(sentences_list, names_list, parsed_args["windowsize"])
                        task_6_output = format_result_to_json(pairs, parsed_args["threshold"])
                        joined_pairs = dict_processing(task_6_output)
                        adj_list = making_adjacency_list(joined_pairs)
                        graph = Graph(adj_list)
                        result = graph.all_the_connections(keys, parsed_args["fixed_length"])
                        print(graph.generate_result_file(result))
                    else : sys.exit("Invalid Input")
                elif parsed_args["sentences"] and parsed_args["names"] and parsed_args["removewords"] and parsed_args["qsek_query_path"] and parsed_args["fixed_length"] >= 0 and parsed_args["windowsize"] ==0 and parsed_args["threshold"]>= 0  :
                    dict = initial_text_processing(parsed_args["sentences"], parsed_args["names"], parsed_args["removewords"])
                    sentences_list = dict_to_list(dict)
                    names_list = process_data_from_dict(dict)
                    pairs = pairs_occurrences(sentences_list, names_list, parsed_args["windowsize"])
                    task_6_output = format_result_to_json(pairs, parsed_args["threshold"])
                    joined_pairs = dict_processing(task_6_output)
                    adj_list = making_adjacency_list(joined_pairs)
                    graph = Graph(adj_list)
                    print(graph.generate_result_file([]))
                else : sys.exit("Invalid Input")
            case 9 :
                if parsed_args["preprocessed"] and parsed_args["threshold"] :
                    parsed_args["preprocessed"] = r'.\output.json'
                    dictionary = open_file(parsed_args["preprocessed"])
                    sentences_list = dict_to_list(dictionary)
                    result = UnionFind.common_words(sentences_list, parsed_args["threshold"])
                    json_result = json.dumps(result, indent=4)
                    print(json_result)
                elif parsed_args["sentences"] and parsed_args["removewords"] and parsed_args["threshold"]:
                    with open("names_file.csv", "w") as names_file:
                        pass
                    file_path = os.path.abspath("names_file.csv")
                    dictionary = initial_text_processing(parsed_args["sentences"], file_path, parsed_args["removewords"])
                    sentences_list = dict_to_list(dictionary)
                    result = UnionFind.common_words(sentences_list, parsed_args["threshold"])
                    json_result = json.dumps(result, indent=4)
                    print(json_result)
                else : sys.exit("Invalid Input")
    except Exception as e :
        sys.exit("Invalid Input")


def main():
    try :
        parser = readargs()
        valid_args(vars(parser.parse_args()))

        functions_calling(vars(parser.parse_args()))
    except Exception as e :
        sys.exit("Invalid Input")

if __name__=="__main__":
    main()

