class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # cost actually means (how many numbers if the cost is 1)
        # [1,3,5,2] is actually [1,1,3,3,3,5,2,2,2,2,2,....]
        # so we just need to find the median of the expanded unweighted list

        total = sum(cost)
        n = len(nums)


        s = [(nums[i], cost[i]) for i in range(n)]
        s.sort()

        c = 0
        target = 0

        for i in range(n):
            c += s[i][1]
            if c > total//2: #median
                target = s[i][0]
                break
        ans = 0

        for i in range(n):
            ans += abs((nums[i] - target)) * cost[i]

        return ans
