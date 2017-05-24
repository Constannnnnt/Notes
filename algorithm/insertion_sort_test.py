# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    module: insertion sort
'''
from insertion_sort import insertion_sort

if __name__ == '__main__':
    print(insertion_sort([1, 5, 10, 2, 12, 20]))
    print(insertion_sort([1, 5, 10, 2, 12, 20], 'descending'))
    print(insertion_sort([1, 5, 10, 2, 12, 20], 'invalid input'))
    print(insertion_sort([1, 'a', 10, 2, 'A', 20]))
    print(insertion_sort([1, 'a', 10, 2, 'A', 20], 'descending'))
