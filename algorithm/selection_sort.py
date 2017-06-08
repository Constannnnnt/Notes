# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    No modules
'''

def selection_sort(arr, direction=None):
    '''
        algorithm:
        Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
        The algorithm proceeds by
            1. finding the smallest (or largest) element in the unsorted sublist
            2. putting it in sorted order,
            3. moving the sublist boundaries one element to the right.
            
        complexity in O(n^2)
    '''
    if (direction == 'descending'):
        for i in range(len(arr)):
            maxBound = i
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[i]:
                    maxBound = j
            arr[i], arr[maxBound] = arr[maxBound], arr[i]
        return arr
    else:
        for i in range(len(arr)):
            minBound = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    minBound = j
            arr[i], arr[minBound] = arr[minBound], arr[i]
        return arr
