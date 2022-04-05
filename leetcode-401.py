class Solution:

    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        s = [1,2,4,8,16,32,1,2,4,8]

        res = []

        def dfs(remain, cur, h, m):

            if h > 11 or m > 59 :
                return # not valid time

            if remain == 0:
                res.append('%d:%02d'%(h,m))
                return

            for i in range(cur, len(s)):

                #indx[i] = True

                if i > 5:
                    dfs(remain-1, i + 1, h + s[i], m )
                else:
                    dfs(remain-1, i + 1, h, m + s[i])

        dfs(turnedOn,0,0,0)

        return res
