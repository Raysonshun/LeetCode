class Solution:
    def divisorGame(self, n: int) -> bool:

        if n == 1:
            return 0
        if n == 2:
            return 1

        dp = [0 for i in range(n+1)]

        dp[1] = 0
        dp[2] = 1

        for i in range(3,n+1):
            for j in range(1,i):

                if i%j == 0 and dp[i-j] == 0:
                    dp[i] = 1

        return dp[n]