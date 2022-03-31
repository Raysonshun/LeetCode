class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)
        s = []
        visited = []

        ''' my solution
        def repeat(s):
            if len(set(s)) == len(s):
                return 1
            else:
                return 0

        def dfs(s):

            if len(s) == n:
                if repeat(s):
                    res.append(s[:])

            if len(s) >=n:
                return

            for i in range(n):

                s.append(nums[i])
                dfs(s)
                s.pop()

        dfs(s)
        return res
        '''
        # Another Solution

        def dfs(s):

            if len(s) == n:
                res.append(s[:])
            if len(s) >= n:
                return

            for i in range(n):
                if nums[i] not in s:
                    s.append(nums[i])
                    dfs(s)
                    s.pop()

        dfs(s)
        return res