"""
    Loads in the JSON data from "minerals/mineral_data/minerals.json"
    Creates A Mineral instance for each entry in the json fil
"""

import json
import os


CURRENT_DIR = os.getcwd()
INITIAL_DATA_PATH = "{}/minerals/mineral_data/minerals.json".format(CURRENT_DIR)
TEST_DATA_PATH = "{}/minerals/mineral_data/test.json".format(CURRENT_DIR)


def replace_whitespace(mineral_dict):
    """Replaces whitespace with underscores so that keys match the Model fields"""
    new_dict = {}
    for key in mineral_dict:
        if len(key) == 1:
            new_dict[key] = mineral_dict[key]
        else:
            new_key = key.replace(' ', '_')
            new_dict[new_key] = mineral_dict[key]
    return new_dict


def load_initial_data():
    with open(TEST_DATA_PATH, 'r') as json_file:
        data = json.load(json_file)
        for line in data:
            new_dict = replace_whitespace(line)
            print(new_dict)


if __name__ == "__main__":
    load_initial_data()
