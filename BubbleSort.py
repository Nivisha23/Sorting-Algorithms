#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:01:56 2021

@author: Nivisha
"""

arr = [34, 23, 76, 56, 98, 34, 20, 10, 36]
print(arr)

for i in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
print(arr)
