class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        n = len(nums)

        if n <= 2:
            return []

        nums.sort()

        indx = 0

        for i in range(n):

            target = 0 - nums[i]

            j = i + 1
            k = n - 1

            while (j < k):

                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

        #res = set(res)

        return res