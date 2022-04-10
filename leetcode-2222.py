class Solution:
    def numberOfWays(self, s: str) -> int:

#         res = []
#         cur = []
#         n = len(s)

#         def dfs(cur,start,l):

#             # if len(cur) > 1 and cur[-1] == cur[-2]:
#             #     return

#             if l == 3:
#                 res.append(cur)
#                 return

#             if l < 3:

#                 for i in range(start,n):
#                         if (not cur) or (cur and s[i]!=cur[-1]):
#                             cur.append(s[i])
#                             dfs(cur,i + 1, l + 1)
#                             cur.pop()
#                         else:
#                             continue
#         dfs(cur,0,0)
#         return len(res)

        n = len(s)
        c0, c1, dp10, dp01, dp = 0, 0, 0, 0, 0
        for i in range(n):
            if s[i] == '0':
                dp += dp01
                c0 += 1
                dp10 += c1
            else:
                dp += dp10
                c1 += 1
                dp01 += c0
        return dp