class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        s = []

        nums = [(-nums[i],i) for i in range(len(nums))]

        heapify(nums)

        while(len(s) < k):
            val, indx = heappop(nums)
            s.append((-val,indx))

        res = []

        s = sorted(s, key = lambda x:x[1])

        for i in s:
            res.append(i[0])

        return res