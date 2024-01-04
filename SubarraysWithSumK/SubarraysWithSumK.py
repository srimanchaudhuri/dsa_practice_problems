from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    # Write your code here.
    pre_sum_dict = {0:1}
    pre_sum = 0
    pre_cnt = 0
    cnt = 0
    sum = 0
    for i in arr:
        sum += i
        if pre_sum_dict.get(sum-s) != None:
            cnt += pre_sum_dict.get(sum-s)
        if pre_sum_dict.get(sum)!= None:
            pre_sum_dict[sum] += 1
        else:
            pre_sum_dict[sum] = 1
    return cnt
    pass
