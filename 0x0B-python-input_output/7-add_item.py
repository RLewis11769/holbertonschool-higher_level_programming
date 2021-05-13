#!/usr/bin/python3

""" Add items via command line - sys.argv[] """
import json
import sys

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from("add_item.json")
except:
    new_list = []

for x in range(1, len(sys.argv)):
    new_list.append(sys.argv[x])

save_to(new_list, "add_item.json")
