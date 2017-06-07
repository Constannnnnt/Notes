# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    No modules
'''

def merge_sort(arr, direction=None):
    '''
        algorithm: divide the unsorted list into n sublists, each containing 1 element
        (a list of 1 element is considered sorted), then repeatedly merge sublists to
        produce new sorted sublists until there is only 1 sublist remaining
    '''
    if direction == 'descending':
        if len(arr) <= 1:
            return arr
        mid = int(len(arr) / 2)
        left_arr = merge_sort(arr[:mid], 'descending')
        right_arr = merge_sort(arr[mid:], 'descending')
        return merge_des(left_arr, right_arr)
    else:
        if len(arr) <= 1:
            return arr
        mid = int(len(arr) / 2)
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])
        return merge(left_arr, right_arr)

def merge(left, right):
    '''
        merge two halves arrs
    '''
    arr = []
    l, r = 0, 0

    # compare elements in left arr and right arr if possible
    while (l < len(left)) and (r < len(right)):
        if left[l] <= right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1

    # for the remaining elements
    for i in range(l, len(left)):
        arr.append(left[i])
    for i in range(r, len(right)):
        arr.append(right[i])

    return arr

def merge_des(left, right):
    '''
        merge two halves arrs
    '''
    arr = []
    l, r = 0, 0

    # compare elements in left arr and right arr if possible
    while (l < len(left)) and (r < len(right)):
        if left[l] > right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1

    # for the remaining elements
    for i in range(l, len(left)):
        arr.append(left[i])
    for i in range(r, len(right)):
        arr.append(right[i])

    return arr
    