# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    module: insertion sort
'''
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

if __name__ == '__main__':
    # tests for insertion_sort
    print('-----insertion sort-----')
    print(insertion_sort([1, 5, 10, 2, 12, 20]))
    print(insertion_sort([1, 5, 10, 2, 12, 20], 'descending'))
    print(insertion_sort([1, 5, 10, 2, 12, 20], 'invalid input'))
    print()

    # tests for bubble_sort
    print('-----bubble sort-----')
    print(bubble_sort([1, 5, 10, 2, 12, 20]))
    print(bubble_sort([1, 5, 10, 2, 12, 20], 'descending'))
    print(bubble_sort([1, 5, 10, 2, 12, 20], 'invalid input'))
    print()
    # tests for quick_sort
    print('-----quick sort-----')
    print()
    # tests for merge_sort
    print('-----merge sort-----')
    print()
