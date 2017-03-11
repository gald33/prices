# -*- coding: UTF-8 -*-

import json
from pprint import pprint

branches_json_filename = "branches.json"
branches_list = []
branches_downloaded = []


def get_branches_data():
    with open(branches_json_filename) as f:
        branches_data = json.load(f)
    return branches_data


def string(branch):
    return "PriceFull" + branch["chain_id"] + "-" + branch["branch_id"] + "-"


def branch_list():
    for branch in get_branches_data():
        branches_list.append(string(branch))
    return branches_list


def get_undownloaded_branches():
    return list(set(branches_list) - set(branches_downloaded))


def info():
    # pprint("Branches:")
    # pprint(branches_list)
    # pprint("Branches downloaded:")
    # pprint(branches_downloaded)
    undownloaded_branches = get_undownloaded_branches()
    if undownloaded_branches is not []:
        text = "Branches not downloaded:\n"
    	for branch in undownloaded_branches:
    		text += branch + "\n"
    	return text
    else:
    	text = "All branches downloaded"


if __name__ == "__main__":
    pprint(branch_list())
