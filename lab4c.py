#!/usr/bin/env python3

def create_dictionary(keys, values):
    return dict(zip(keys, values))

def shared_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())

if __name__ == '__main__':
    pass
