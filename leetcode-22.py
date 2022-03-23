class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(l,r,output):

            if l == r == n:

                res.append(output)

                return

            if l < n:

                backtrack(l+1, r, output + '(')

            if l > r:

                backtrack(l, r+1, output + ')')



        backtrack(0,0,'')

        return res
