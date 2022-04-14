class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        n = len(nums)

        diff = float('Inf')

        for i in range(n):

            start = i + 1

            end = n - 1

            while (start < end):

                cur = nums[i] + nums[start] + nums[end]

                if abs(cur - target) < abs(diff):

                    diff = cur - target

                if cur == target:
                    return cur

                elif cur < target:

                    start += 1

                else:

                    end -= 1

        return target + diff