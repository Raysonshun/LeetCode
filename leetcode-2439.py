class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mn = nums[0]
        nums = list(accumulate(nums))
        for i, n in enumerate(nums):
            mn = max(mn, ceil(n/(i+1)))
        return mn