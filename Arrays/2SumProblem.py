'''
STEPS TO SOLVE
-> At first sort the array
-> We solve this problem using a 2-pointer approach
-> We keep a left and right pointer at 0 and the nth index of the array
-> We iterate through the array till the left pointer is not greater than the right pointer
-> We increase the left pointer if the sum exceeds the target to find and vice versa
-> We return 'YES' if the target is found
-> We return 'NO' at the end of the loop if the target is not found
'''

def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    book.sort()
    left = 0
    right = n-1
    while left <= right:
        if book[left]+book[right] == target:
            return 'YES'
        elif book[left]+book[right] < target:
            left = left+1
        else:
            right = right - 1;
    return 'NO'
    pass
