class Solution(object):
    def combSum(self, ind, target, subs, a, ans):
        if ind == len(a):
            if target == 0:
                ans.append(subs[:])
            return
        if a[ind] <= target:
            subs.append(a[ind])
            self.combSum(ind, target - a[ind], subs, a, ans)
            subs.pop()
        self.combSum(ind + 1, target, subs, a, ans)
        
    def combinationSum(self, candidates, target):
        ans = []
        self.combSum(0, target, [], candidates, ans)
        return ans
