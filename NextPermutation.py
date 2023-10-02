'''
Intuition is based on a dictionary arrangement 
Where we arrange item as per a prefix and then arrange from smallest to biggest 
Eg. like sad,sat,sit (here sa is the prefix and order is determined by d and t)

Steps -> 
1) Search for a breakpoint (breakpoint is where Previous element is smaller then the current element)
2) Once got the bbreakpoint traverse the array from last to bp and swap if the first greater number you get with the break point number (0 to bp part of array is like our prefix)
3) Resverse the part of array after break point (because we alredy have that part sorted in descending and if we reverse we will get ascending order which is minimum)
'''


def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    bp = -1
    for i in range(len(A)-1, 1, -1):
        if A[i-1] < A[i]:
            bp = i-1
            break
    if bp == -1:
        return A[::-1]
    for i in range(len(A)-1, bp, -1):
        if A[i]>A[bp]:
            A[i], A[bp] = A[bp], A[i]
            break
    A = A[0:bp+1] + A[-1:bp:-1]
    return A
