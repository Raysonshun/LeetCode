class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        m = [10**4 for i in range(amount+1)]

        for i in coins:
            if i <= amount:
                m[i] = 1

        if amount == 0:
            return 0

        for i in range(len(m)):
            for j in coins:
                if i >= j:
                    m[i] = min(m[i], m[i-j] + 1)

        if m[amount] != 10**4:
            return m[amount]
        else:
            return -1