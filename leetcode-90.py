class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = [[]]
        n = len(nums)
        indx = [False for i in nums]


        def dfs(s,start):

            if start >= n:
                return

            for i in range(start, n):

                s.append(nums[i])
                if s not in res:
                    res.append(s[:])
                dfs(s, i + 1)
                s.pop()

        dfs([],0)

        return res