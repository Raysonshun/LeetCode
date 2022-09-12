class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        visit = set()
        occur = {}

        for i in range(len(s)):
            occur[s[i]] = i

        for i in range(len(s)):

            cur = s[i]

            if cur not in visit:
                while (stack and stack[-1] > s[i] and occur[stack[-1]] > i):
                    temp = stack.pop()

                    visit.remove(temp)

                stack.append(cur)
                visit.add(cur)
                print(stack)

        return ''.join(stack)

        #https://leetcode.com/problems/remove-duplicate-letters/discuss/1859515/Python-oror-O(n)-Beats-98-oror-Stack-oror-Detailed-Explanation-oror-Simple