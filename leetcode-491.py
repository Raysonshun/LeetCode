class Solution:

    #''' my code
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = set()
        indx = [False for i in nums]

        def dfs(s, start, l):

            if l > len(nums):
                return

            for i in range(start, len(nums)):

                cur = nums[i]

                if s and cur < s[-1]:
                    continue

                s.append(cur)

                if len(s)>1: res.add(tuple(s))

                dfs(s,i+1, l + 1)

                s.pop()

        dfs([], 0,0)

        return res
        #'''

    # others

#     def findSubsequences(self, A: List[int]) -> List[List[int]]:
#         result, N = set(), len(A)

#         def backtrack(curr, index):
#             if index == N: return
#             for i in range(index, N):
#                 c = A[i]
#                 if curr and c < curr[-1]: continue

#                 curr.append(c)
#                 if len(curr) > 1: result.add(tuple(curr))
#                 backtrack(curr, i + 1)
#                 curr.pop()

#         backtrack([], 0)
#         return result