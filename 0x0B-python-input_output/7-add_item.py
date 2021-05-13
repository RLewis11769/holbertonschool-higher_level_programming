#!/usr/bin/python3

""" Loads, adds, and saves command arguments to new file """

import json
import sys

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

""" Adds existing file info to new_list """
try:
    new_list = load_from("add_item.json")
except:
    new_list = []

""" Adds command line arguments to new_list """
for x in range(1, len(sys.argv)):
    new_list.append(sys.argv[x])

save_to(new_list, "add_item.json")
