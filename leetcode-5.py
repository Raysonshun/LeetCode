class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)


        def isp(start, end):   # use current [start:end] as starting point, and expand both to the left and right as long as possible until it's not a palindrome number any more

            while (0<=start<n and 0<=end<n and s[start] == s[end]):
                start -= 1
                end += 1

            return s[start+1:end]

        res = ''

        for i in range(n):

            l1 = isp(i,i)     # center point is 1 number - total length is odd
            l2 = isp(i,i+1)    # center point is 2 numbers - total length is even

            if max(len(l1), len(l2))> len(res):

                if len(l1) > len(l2):
                    res = l1
                else:
                    res = l2

        return res