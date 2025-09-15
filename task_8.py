import json
from typing import Optional
from task_1 import *
import sys

class Graph:
    def __init__(self: "Graph", adj_list: Optional[dict] = None) -> None:
        self.adj_list = adj_list if adj_list else {}

    def is_connected_by_path_of_length(self: "Graph", start: str, end: str, fixed_length: int)->bool:
        # this function returns True if two nodes are reached within the given fixed length
        def dfs(node: str, target: str, remaining_length: int, visited: set) -> bool:
            # this function run dfs on the graph
            if remaining_length == 0:
                return node == target

            visited.add(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited: # running dfs on nodes that have not been reached yet
                    if dfs(neighbor, target, remaining_length - 1, visited.copy()):
                        return True

            return False

        return dfs(start, end, fixed_length, set())

    def all_the_connections(self: "Graph", keys_dict: dict[str,list[list[str]]], fixed_length: int)-> list[list[bool| str]]:
        ''' this function returns true if there's a path from fixed_length
            and false if there is no path from fixed_length
        '''
        try :
            result_list =[]
            keys_list = keys_dict["keys"]
            for i in range(len(keys_list)) :
                start = keys_list[i][0]
                end = keys_list[i][1]
                if self.is_connected_by_path_of_length(start, end, fixed_length):
                    result_list.append(sorted([start, end]) + [True]) # sorting the names alphabetically
                else :
                    result_list.append(sorted([start, end]) + [False])
            result_list.sort(key=lambda x: (x[0], x[1], x[2]))  # sorting the names
            return result_list
        except  Exception as e:
            sys.exit("Invalid Input")

    def generate_result_file(self: "Graph",result_list: list[list[bool| str]])-> str:
        # this function forms the result file and dumps it
        try :
            formatted_data = [[name1, name2, str(value).lower() == "true"] for name1, name2, value in result_list]
            output_json = {
                "Question 8": {
                    "Pair Matches": formatted_data
                }
            }
            # Write to a JSON file
            with open("output.json", "w") as json_file:
                json.dump(output_json, json_file, indent=4)
            return json.dumps(output_json, indent=4)
        except Exception as e:
            sys.exit("Invalid Input")
