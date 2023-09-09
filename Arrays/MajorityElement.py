'''
STEPS TO SOLVE:
1) USE NOOR's VOTING ALGORITHM

-> Pick first element as the majority element
-> Start iterating through the array
-> If the current element is same as the picked element(ele in the code) increase count by 1
-> If not then decrease count by 1
-> I the count goes down to zero change the picked element to the current element
-> Because is the count is canceled to zero then the element could never be the majority element till that portion of the array

2) Check weter the majority element through NOOR's Voting Algorithm is actually the majority element

-> Iterate the array
-> Count the number of times the element occurs in the array
-> If count is greater then N/2 times then that is the majority element
'''

def majorityElement(v: [int]) -> int:
    # Write your code here
    ele = v[0]
    count = 0
    for i in v:
        if ele == i:
            count += 1
        else:
            count -= 1
        if count == 0:
            ele = i
            count += 1
    count = 0
    for i in v:
        if ele == i:
            count += 1
    if count > (len(v)/2):
        return ele
    pass
