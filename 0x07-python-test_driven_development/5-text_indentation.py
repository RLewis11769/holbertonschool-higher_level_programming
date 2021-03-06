#!/usr/bin/python3

"""
text_indentation - prints text with new line after each . ? and :
@text: single string to add newlines to
"""


def text_indentation(text):
    """ Adds newlines after each ".", "?", and ":" """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str1 = ""
    new_str2 = ""
    final_str = ""

    split_at_p = text.split(".")
    for phrase in range(len(split_at_p)):
        """ Phrase is entire string between . """
        for char in range(len(split_at_p[phrase])):
            """ Removes spaces from front of string """
            if split_at_p[phrase][char] != " ":
                split_at_p[phrase] = split_at_p[phrase][char:]
                break
        """ Adds newlines to end of string unless last line """
        if phrase < len(split_at_p) - 1:
            new_str1 += split_at_p[phrase] + ".\n\n"
        else:
            new_str1 += split_at_p[phrase]

    split_at_q = new_str1.split("?")
    for phrase in range(len(split_at_q)):
        for char in range(len(split_at_q[phrase])):
            if split_at_q[phrase][char] != " ":
                split_at_q[phrase] = split_at_q[phrase][char:]
                break
        if phrase < len(split_at_q) - 1:
            new_str2 += split_at_q[phrase] + "?\n\n"
        else:
            new_str2 += split_at_q[phrase]

    split_at_c = new_str2.split(":")
    for phrase in range(len(split_at_c)):
        for char in range(len(split_at_c[phrase])):
            if split_at_c[phrase][char] != " ":
                split_at_c[phrase] = split_at_c[phrase][char:]
                break
        if phrase < len(split_at_c) - 1:
            final_str += split_at_c[phrase] + ":\n\n"
        else:
            final_str += split_at_c[phrase]

    print("{}".format(final_str), end="")
