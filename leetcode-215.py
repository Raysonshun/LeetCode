class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq as hq

        hq.heapify(nums)

        while (len(nums) > k):
            hq.heappop(nums)

        return nums[0]