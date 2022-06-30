class Solution:
    def totalFruit(self, fruits: List[int]) -> int:


        # sliding window:

        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(fruits)):
            nums[fruits[r]] += 1
            while len(nums) > 2:
                nums[fruits[l]] -= 1
                if not nums[fruits[l]]:
                    nums.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res

#     '''
#     My Solution

#         n = len(fruits)
#         res = [0 for i in range(n)]

#         if n == 1:return 1
#         if n ==2: return 2

#         res[0] = 1

#         pre = fruits[0]
#         pre_c = 1
#         cur_c = 0

#         for i in range(1,n):

#             if fruits[i] == pre:
#                 res[i] = res[i-1] + 1
#                 pre_c += 1
#                 continue
#             else:
#                 indx = i
#                 cur = fruits[i]
#                 res[i] = res[i-1] + 1
#                 cur_c += 1
#                 break

#         if cur_c == 0:
#             return n

#         for i in range(indx + 1, n):

#             if fruits[i] == pre:
#                 pre_c = cur_c
#                 cur_c = 1
#                 pre, cur = cur, pre
#                 res[i] = res[i-1] + 1
#             elif fruits[i] == cur:
#                 cur_c += 1
#                 res[i] = res[i-1] + 1
#             else:
#                 pre, cur = cur, fruits[i]
#                 pre_c, cur_c = cur_c, 1
#                 res[i] = pre_c + 1

#         return max(res)
