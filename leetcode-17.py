class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)

        summ = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

        res = []

        if n == 1:
            return summ[digits[0]]
        if n == 0:
            return []

        marker = 1
        #I'm just trying if changes work or not for github push

        for i in digits:

            digit = summ[i]
            tmp = res.copy()


            if len(res) == 0:

                for x in digit:
                    res.append(x)

            else:
                for k in tmp:
                    for char in digit:
                        res.append(k + char)

        n2 = len(res)
        res2 = []

        for i in range(n2):
            if len(res[i]) == n:
                res2.append(res[i])
        return res2
