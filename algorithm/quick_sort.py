# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    No modules
'''

def quick_sort(arr, head, tail, direction=None):
    '''
        algorithm: partition an array into two parts such that all elements in one part
        is smaller than every element in another part. Then, use recursion to partition
        the following parts.
    '''

    if (direction == 'descending'):
        if head < tail:
            mid = partition_des(arr, head, tail)
            quick_sort(arr, head, mid - 1, 'descending')
            quick_sort(arr, mid + 1, tail, 'descending')
    else:
        if head < tail:
            mid = partition(arr, head, tail)
            quick_sort(arr, head, mid - 1)
            quick_sort(arr, mid + 1, tail)

def partition_des(arr, head, tail):
    '''
        partition the arr into two parts for descending array
    '''
    cur = head
    for pos in range(head, tail):
        if arr[pos] > arr[tail]:
            arr[pos], arr[cur] = arr[cur], arr[pos]
            cur += 1
    arr[cur], arr[tail] = arr[tail], arr[cur]
    return cur

def partition(arr, head, tail):
    '''
        partition the arr into two parts for ascending array
    '''
    cur = head
    for pos in range(head, tail):
        if arr[pos] < arr[tail]:
            arr[pos], arr[cur] = arr[cur], arr[pos]
            cur += 1
    arr[cur], arr[tail] = arr[tail], arr[cur]
    return cur
