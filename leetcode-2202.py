class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:


        n = len(nums)

        if k == 0:
            return nums[0]

        if n ==1 and k%2 == 1:
            return -1

        if k > len(nums):
            return max(nums)

        if k ==1:
            return nums[1]

        maxx = max(nums[0:k-1])

        if k < n:
            maxx1 = nums[k]
        else:
            maxx1 = -1

        return max(maxx,maxx1)