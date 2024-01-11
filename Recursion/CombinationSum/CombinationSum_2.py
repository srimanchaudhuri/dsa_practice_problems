class Solution(object):
    def combSum(self, ind, ds, target, arr, ans, n):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind,n):
            if i > ind and arr[i] == arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.combSum(i+1, ds, target-arr[i], arr, ans, n)
            ds.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.combSum(0,[],target,candidates,ans,len(candidates))
        return ans
        
