class Solution:
    def intToRoman(self, num: int) -> str:

        sym = ['I','II','III','V','X','L','C','D','M','IV', 'IX','XL','XC','CD','CM']
        val = [1,2,3,5,10,50,100,500,1000,4,9,40,90,400,900]

        d = {}

        n = len(sym)

        for i in range(n):
            d[val[i]] = sym[i]

        val.sort()

        res = ''

        for i in range(n-1,-1,-1):

            cur = num//val[i]
            if cur != 0:
                res += d[val[i]] * cur
                num = num - num//val[i] * val[i]

        return res