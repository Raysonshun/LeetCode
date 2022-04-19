class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float('inf')

        n = len(nums)

        l, r = 0,0

        summ = 0

        while(r <= n-1):

            summ += nums[r]

            while(summ >= target):

                res = min(res, r - l + 1)
                summ -= nums[l]
                l += 1

            r += 1

        return res if res != float('inf') else 0
