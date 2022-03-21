class Solution:

    def __init__(self):
        self.res = []
        self.l = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res.append([])

        self.dfss(nums,0)
        return self.res



    def dfss(self,nums: List[int],start):

        if start >= len(nums): return

        for i in range(start,len(nums)):
            self.l.append(nums[i])
            a = [j for j in self.l]
            self.res.append(a)
            print(self.res)
            self.dfss(nums,i + 1)
            self.l.pop()