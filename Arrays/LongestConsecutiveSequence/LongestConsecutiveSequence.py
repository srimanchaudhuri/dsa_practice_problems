def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    a_set = {1}
    a_set.pop()
    count = 0
    counting = 0
    longestCount = -1
    for i in a:
        a_set.add(i) # Formation of set
    for i in a_set:
        if i-1 in a_set: # Check if it is the starting point
            continue;
        else: # If it is the starting point then start counting
            counting = 1 # Denotes counting started
            count = 1 
            currEle = i # Store current Element
            while counting == 1:
                if currEle+1 in a_set: # Check for next consecutive numbers after the current element
                    count += 1
                    currEle += 1
                else:
                    counting = 0 # When the next number is not found just stop counting and check the longest count till now and continue the loop
                    longestCount = max(longestCount, count)
    return longestCount
    pass
