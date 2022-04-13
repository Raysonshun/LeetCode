class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1 for i in range(n)]

        def climb(cur):

            if cur == 1:
                return 1
            if cur == 2:
                return 2

            if memo[cur-1] != -1:
                return memo[cur-1]

            r = climb(cur-1) + climb(cur-2)
            memo[cur-1] = r

            return r

        res = climb(n)

        return res