'''
STEPS TO SOLVE (Kadane's Algorithm)
-> Take variables sum and max and assign them to 0 and arr[0] respectively
-> Iterate through the Array
-> Add the element in sum
-> Check if sum is negative then make the sum 0
-> If sum is positive check if the sum is greater then max value and update the max
-> return max is max is positive
'''

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) -> int:
    sum = 0
    max = arr[0]
    for i in arr:
        sum += i
        if sum < 0:
            sum = 0
        else:
            if sum > max:
                max = sum
    if max > 0:
        return max
    else:
        return 0
