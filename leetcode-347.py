class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        nums = list(set(nums))

        for i in range(len(nums)):
            nums[i] = (d[nums[i]], nums[i])

        heapq.heapify(nums)

        while(len(nums) >  k):
            heapq.heappop(nums)

        res = [nums[i][1] for i in range(len(nums))]

        return res