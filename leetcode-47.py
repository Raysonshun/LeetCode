class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ''' First submission
        res = []
        ad = []

        def dfs(s, cur_l,used):

            if cur_l == len(nums):
                temp = [str(i) for i in s]
                ad_s = ''.join(temp)
                if ad_s not in ad:
                    ad.append(ad_s)
                    res.append(s[:])
                return

            if cur_l < len(nums):

                for i in range(len(nums)):

                    if i not in used:
                        used.append(i)
                        s.append(nums[i])
                        #print(s)
                        dfs(s,cur_l + 1,used)
                        s.pop()
                        used.pop()

        dfs([],0,[])

        return res '''

        #Second submission
#         res = []

#         def dfs(s, cur_l,used):

#             if cur_l == len(nums) and s not in res:
#                 res.append(s[:])
#                 return


#             for i in range(len(nums)):
#                 if i not in used:
#                     used.append(i)
#                     s.append(nums[i])

#                     dfs(s,cur_l + 1,used)
#                     s.pop()
#                     used.pop()

#         dfs([],0,[])
#         return res

    # third method using counter
    def permuteUnique(self, A):

        def backtrack(a, k):
            if k == n:
                res.append(a.copy())
                return

            for v in counter:
                if counter[v] > 0:
                    a.append(v)
                    counter[v] -= 1
                    backtrack(a, k + 1)
                    counter[v] += 1
                    a.pop()

        res, n, counter = [], len(A), Counter(A)
        backtrack([], 0)
        return res