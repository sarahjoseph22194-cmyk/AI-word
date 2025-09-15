from collections import deque
from typing import Union
import sys
import json

def dict_processing(connection_dictionary: Union[dict[str,dict[str,list[list[list[str]]]]] | str])-> Union[list[list[str]],str]:
    '''
    this function receives the output from task 6 and breaks it down to pairs
    if possible and returns it if it's possible
    if not then it returns Invalid Input
    '''
    try:
        # Parse JSON if input is a string
        connections_dictionary ={}
        if isinstance(connection_dictionary, str):
            # If it ends with .json, treat it as a file path
            # Otherwise, assume it's a JSON string
            connections_dictionary = json.loads(connection_dictionary)
        # Validate structure
        elif  isinstance(connection_dictionary, dict):
            # Input is already a dictionary
            connections_dictionary = connection_dictionary
        if "Question 6" not in connections_dictionary or "Pair Matches" not in connections_dictionary["Question 6"]:
            sys.exit("Invalid Input")

        # Process the data
        pair_matches = connections_dictionary["Question 6"]["Pair Matches"]
        joined_pairs = [[" ".join(inner_list) for inner_list in pair] for pair in pair_matches]
        return joined_pairs
    except Exception as e:
        sys.exit("Invalid Input")

def making_adjacency_list(joined_pairs: list[list[str]])-> dict:
    # this function makes the graph from pairs from the function above
    graph = {}
    for u, v in joined_pairs:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph

def bfs_with_distance(graph: dict, start:str)-> dict[str,list]:
    # this function runs bfs on the graph from the start node parameter
    distance_dict = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        current_distance = distance_dict[current]

        for neighbor in graph[current]:
            if neighbor not in distance_dict:  # If the neighbor hasn't been visited yet
                distance_dict[neighbor] = current_distance + 1
                queue.append(neighbor)

        return distance_dict



def checking_connection(keys_dict: dict[str,list[str,str]], names_connections : list[list[str]],maximal_distance : int)-> Union[list[any], str]:
    ''' this function assembles the results between the people with the result if they
    have a connection in the graph and returns a list with the names sorted and their result
    '''
    try:
        result_list = []
        list_of_lists = keys_dict["keys"]  # keys
        adjacency_list = making_adjacency_list(names_connections)  # graph

        for i in range(len(list_of_lists)):
            start = list_of_lists[i][0]  # first name
            person_two = list_of_lists[i][1]  # second name

            # Check if both names exist in the adjacency list
            if start not in adjacency_list or person_two not in adjacency_list:
                result_list.append(sorted([start, person_two]) + [False])
                continue
            distance_dict = bfs_with_distance(adjacency_list, start)
            if person_two in distance_dict and distance_dict[person_two] <= maximal_distance:
                result_list.append(sorted([start, person_two]) + [True])
            else:
                result_list.append(sorted([start, person_two]) + [False])
        result_list.sort(key=lambda x: (x[0], x[1], x[2]))
        return result_list

    except Exception as e:
        sys.exit("Invalid Input")

def json_format(connections_list: list[any])-> str:
    # this function returns the result in a json format
    result = {
        "Question 7": {
            "Pair Matches": connections_list
        }
    }

    # Convert the result to a JSON string (for printing or saving to a file)
    return json.dumps(result, indent=4)

