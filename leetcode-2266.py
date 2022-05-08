class Solution:
    def countTexts(self, p: str) -> int:

        n = len(p)
        dp = [0 for i in range(n+1)]
        dp[0] = 1

        for i in range(1,n+1):

            dp[i] = dp[i-1]

            if i-2 >= 0 and p[i-1] == p[i-2]:
                dp[i] += dp[i-2]

            if i-3 >=0 and p[i-1] == p[i-2] == p[i-3]:
                dp[i] += dp[i-3]

            #if (p[i-1] in {"7", "9"}):
            if (int(p[i-1]) == 7) or (int(p[i-1]) == 9):
                if i-4 >= 0 and p[i-1] == p[i-2] == p[i-3] == p[i-4]:
                    dp[i] += dp[i-4]

            dp[i] %= (10**9+7)

        return dp[-1]%(10**9+7)

# https://leetcode.com/problems/count-number-of-texts/discuss/2017810/Python-dp-easy-to-understand