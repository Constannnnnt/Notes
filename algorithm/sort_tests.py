# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    module: insertion sort
'''
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort

if __name__ == '__main__':
    # tests for insertion_sort
    array = [1, 5, 10, 2, 12, 20]
    print('-----insertion sort-----')
    print(insertion_sort(array))
    array = [1, 5, 10, 2, 12, 20]
    print(insertion_sort(array, 'descending'))
    array = [1, 5, 10, 2, 12, 20]
    print(insertion_sort(array, 'invalid input'))
    print()

    # tests for bubble_sort
    array = [1, 5, 10, 2, 12, 20]
    print('-----bubble sort-----')
    print(bubble_sort(array))
    array = [1, 5, 10, 2, 12, 20]
    print(bubble_sort(array, 'descending'))
    array = [1, 5, 10, 2, 12, 20]
    print(bubble_sort(array, 'invalid input'))
    print()

    # tests for quick_sort
    arr = [1, 5, 10, 2, 12, 20]
    print('-----quick sort-----')
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
    arr = [1, 5, 10, 2, 12, 20]
    quick_sort(arr, 0, len(arr) - 1, 'descending')
    print(arr)
    print()

    # tests for merge_sort
    arr = [1, 5, 10, 2, 12, 20]
    print('-----merge sort-----')
    print(merge_sort(arr))
    arr = [1, 5, 10, 2, 12, 20]
    print(merge_sort(arr, 'descending'))
    print()
