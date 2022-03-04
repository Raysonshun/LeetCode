class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        res = ''

        a = {}

        for i in s:

            if i not in a:
                a[i] = 1
            else:
                a[i] += 1

        for i in t:

            if i not in a:
                res = i
                break
            else:
                a[i] -= 1

        if res == '':

            for i in s:
                if a[i] != 0:
                    res = i
        return res