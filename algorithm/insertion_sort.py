# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    No modules
'''

def insertion_sort(arr, direction=None):
    '''insertion sort,complexity in O(n^2)'''

    if direction != 'descending':
        # by default, sort is ascending
        for i in range(len(arr)):
            key = arr[i]
            pos = i
            while pos > 0 and arr[pos - 1] > key:
                arr[pos] = arr[pos - 1] # Swap the number down the list
                pos = pos - 1
            arr[pos] = key
    else:
        for i in range(len(arr)):
            key = arr[i]
            pos = i
            while pos > 0 and arr[pos - 1] < key:
                arr[pos] = arr[pos - 1] # Swap the number up in the list
                pos = pos - 1
            arr[pos] = key

    return arr

# # test session
# if __name__ == '__main__':
#     print(insertion_sort([1, 5, 10, 2, 12, 20]))
#     print(insertion_sort([1, 5, 10, 2, 12, 20], 'descending'))
