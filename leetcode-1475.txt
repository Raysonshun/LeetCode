class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stk = []
        m = defaultdict(lambda:0)
        res = [ i for i in prices]

        for i in range(len(prices)):

            while stk and prices[stk[-1]] >= prices[i]:

                res[stk.pop()] -= prices[i]


            stk.append(i)

        return res
