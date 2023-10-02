# Very basic intuition that can be understood from code

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    maxi = -999999
    leaders = []
    for i in range((len(a)-1),-1,-1):
        if maxi<a[i]:
            maxi = a[i]
            leaders.append(a[i])
    return leaders
    pass
