'''
STEPS TO SOLVE
-> We keep three pointer low, mid and high and set them accordingly
-> Itereate while mid <= high
************************************************************************************
-> The Rule is :
>>> From (0 to low-1) there should be all 0s
>>> Form (low to mid-1) there should be all 1s
>>> From (mid to high-1) It can be unsorted i.e. containing 0's, 1's & 2's randomly
>>> From (high to n-1) there should be only 2's
************************************************************************************
-> So basically our task is to sort the unsorted portion of mid to high-1 
-> Which we do by the 3 conditional statements as written in the code
'''

from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr,n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
