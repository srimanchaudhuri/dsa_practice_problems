from typing import List

def genSubs(ind: int, sub: str, ans: List[str], s: str):
    if ind >= len(s):
        ans.append(sub)
        return
    sub = sub + s[ind]
    genSubs(ind + 1, sub, ans, s)
    sub = sub[:-1]
    genSubs(ind + 1, sub, ans, s)

def generateSubsequences(s: str) -> List[str]:
    ans = []
    genSubs(0, '', ans, s)
    return ans
