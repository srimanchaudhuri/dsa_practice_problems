# Alternate Numbers
# Basic Intuition is to iterate and place the positive numbers on even indexs and negitive numbers in the odd indexes
# Such that they are still in the order of the given array

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    even = 0
    odd = 1
    ans = [0]*len(a)
    for i in a:
        if i >= 0:
           ans[even] = i
           even += 2
        else:
            ans[odd] = i
            odd += 2
    return ans
