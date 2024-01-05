def getSubs(ind: int, subs: [int], s: int, k: int, a: [int], ans: [[int]]):
    if ind >= len(a):
        if s == k:
            ans.append(subs[:])  # Use a copy of subs
        return
    subs.append(a[ind])
    s = s + a[ind]
    getSubs(ind + 1, subs, s, k, a, ans)
    s = s - a[ind]
    subs.pop()
    getSubs(ind + 1, subs, s, k, a, ans)

def subSequenceWithSumK(a: [int], k: int) -> [[int]]:
    ans = []
    getSubs(0, [], 0, k, a, ans)
    print(f"{ans}\n \n")
    return ans


