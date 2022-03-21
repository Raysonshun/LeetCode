class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = []
        self.l = []
        self.dfs(nums,0)
        ans = 0
        for i in range(len(self.res)):
            ans = ans + self.listXor(self.res[i])
        return ans



    def dfs(self,nums,start):
        if start == len(nums):return
        for i in range(start,len(nums)):
            self.l.append(nums[i])
            a = [j for j in self.l]
            self.res.append(a)
            self.dfs(nums,i+1)
            self.l.pop()


    def listXor(self,a):
        n = len(a)
        if n == 1:
            return a[0]
        res = a[0]
        for i in range(1,n):
            res = a[i]^res
        return res
