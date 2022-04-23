class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)

        l = 0

        for i in num:

            if i-1 not in num:

                cur = i
                c = 0

                while(cur in num):
                    cur += 1
                    c += 1

                l = max(l, c)

        return l