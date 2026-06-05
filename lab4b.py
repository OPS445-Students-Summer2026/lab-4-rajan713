#!/usr/bin/env python3

def join_lists(list1, list2):
    return list(set(list1) | set(list2))

def match_lists(list1, list2):
    return list(set(list1) & set(list2))

def diff_lists(list1, list2):
    return list(set(list1) ^ set(list2))

if __name__ == '__main__':
    pass
