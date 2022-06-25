class Solution:
    def maximumXOR(self, nums: List[int]) -> int:

        n = len(nums)
        res = nums[0]

        for i in range(1,n):
            res = res | nums[i]

        return res

    # https://leetcode.com/problems/maximum-xor-after-operations/discuss/2196139/Intuition-Explained-in-Detail-or-Observation
