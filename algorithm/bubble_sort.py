# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    No modules
'''

def bubble_sort(arr, direction=None):
    '''
        algorithm: by default, sort the array in ascending order, for arr[j],
        compare its neighbor: if arr[j+1] < arr[j], the swap them
    '''

    if direction == 'descending':
        arrlen = len(arr)
        while arrlen > 0:
            for i in range(arrlen - 1):
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            arrlen -= 1
    else:
        direction = 'ascending'
        arrlen = len(arr)
        while arrlen > 0:
            for i in range(arrlen - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            arrlen -= 1
    return arr, direction
