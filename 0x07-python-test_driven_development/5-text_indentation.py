#!/usr/bin/python3

"""
text_indentation - prints text with new line added after . ? and :
@text: string to add new lines to
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str1 = ""
    new_str2 = ""
    final_str = ""

    split_at_p = text.split(".")
    for phrase in range(len(split_at_p)):
        if phrase < len(split_at_p) - 1:
            new_str1 += split_at_p[phrase] + ".\n\n"
        else:
            new_str1 += split_at_p[phrase]

    split_at_q = new_str1.split("?")
    for phrase in range(len(split_at_q)):
        if phrase < len(split_at_q) - 1:
            new_str2 += split_at_q[phrase] + "?\n\n"
        else:
            new_str2 += split_at_q[phrase]

    split_at_c = new_str2.split(":")
    for phrase in range(len(split_at_c)):
        if phrase < len(split_at_c) - 1:
            final_str += split_at_c[phrase] + ":\n\n"
        else:
            final_str += split_at_c[phrase]

    print("{}".format(final_str), end="")
