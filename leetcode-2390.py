class Solution:
    def removeStars(self, s: str) -> str:

    # Binary Search
        n = len(s)

        ns = []
        st = []

        for i in range(n):
            if s[i] == '*':
                st.append(i)
            else:
                ns.append(i)

        for i in range(len(st)):
            cur = st[i]
            cur_l = bisect_right(ns,cur)
            ns.pop(cur_l-1)

        ans = ''
        for i in range(len(ns)):
            ans += s[ns[i]]

        return ans

    # Stack Solution
#     def removeStars(self, s: str) -> str:

#         stack = []

#         for char in s:
#             if char != '*':
#                 stack.append(char)
#             else:
#                 stack.pop()

#         return "".join(stack)