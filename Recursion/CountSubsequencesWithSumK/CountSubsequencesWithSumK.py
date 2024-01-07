def getSubs(ind: int, subs: [int], s: int, k: int, a: [int]) -> int:
    if ind >= len(a):
        if s == k:
            return 1  # Use a copy of subs
        return 0
    subs.append(a[ind])
    s = s + a[ind]
    l = getSubs(ind + 1, subs, s, k, a)
    s = s - a[ind]
    subs.pop()
    r = getSubs(ind + 1, subs, s, k, a)
    return l + r

def subarraysWithSumK(a: [int], k: int) -> int:
    return getSubs(0, [], 0, k, a)
