def getSubs(ind: int, s: int, k: int, a: [int]) -> bool:
    if ind >= len(a):
        if s == k:
            return True  # Use a copy of subs
        return False
    s = s + a[ind]
    if getSubs(ind + 1, s, k, a):
        return True
    s = s - a[ind]
    if getSubs(ind + 1, s, k, a):
        return True
    return False

def subarraysWithSumK(a: [int], k: int) -> True:
    return getSubs(0, 0, k, a)
