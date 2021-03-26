#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 04:36:21 2021

@author: Nivisha
"""

arr = [34, 23, 76, 56, 98, 34, 20, 10, 36]
print(arr)

def quick_sort(arr):
    
    less, greater = [], []

    if len(arr) <= 1:
        return arr

    else:
        for i in arr:
            if i >= arr[-1]:
                greater.append(i)
            else:
                less.append(i)
                break
        return [quick_sort(less), quick_sort(greater)]
    
        
            

def some():
    print(quick_sort(arr))



some()