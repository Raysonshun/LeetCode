class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) == k:
            return '0'

        stack = []

        for i in num:

            while (stack and k and int(i) < stack[-1]):

                stack.pop()
                k -= 1
            stack.append(int(i))

        while (k):
            stack.pop()
            k -= 1

        return str(int(''.join([str(i) for i in stack]))) if stack else '0'