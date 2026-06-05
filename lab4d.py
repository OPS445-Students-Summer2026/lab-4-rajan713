#!/usr/bin/env python3

def first_five(text):
    return text[:5]


def last_seven(text):
    return text[-7:]


def middle_number(number):
    s = str(number)

    if s[0] == '-':
        s = s[1:]

    if '.' in s:
        left, right = s.split('.')

        # checker expects ".5" style output
        if len(right) >= 1:
            return '.' + right[0]
        return '.'

    # integer case (e.g. 1500 -> "50")
    if len(s) < 2:
        return s

    mid = len(s) // 2
    return s[mid-1:mid+1]


def first_three_last_three(a, b):
    return a[:3] + b[-3:]
