#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result_list = set(set_1) ^ set(set_2)
    return result_list
