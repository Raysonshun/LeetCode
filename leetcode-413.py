class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 3: return 0

        dif = 0

        i = 1
        l = 0
        res = 0

        while i < n:

            dif = nums[i] - nums[i-1]

            if i+1 < n and nums[i+1] - nums[i] == dif :

                l = 3
                i = i + 1

                while i+1 < n and nums[i+1] - nums[i] == dif:
                    l += 1
                    i += 1

            if l != 0:
                for j in range(1,l-1):
                    res = res + j
            l = 0

            i = i +1

        return res