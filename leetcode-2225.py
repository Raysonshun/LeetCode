class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        n = len(matches)
        m = 0

        for i in range(n):
            m = max(m, matches[i][0], matches[i][1])

        #print(m)
        d = {}
        l = {}

        for i in range(m + 1):
            d[i] = 0
            l[i] = 0

        for i in range(n):

            d[matches[i][0]] += 1
            l[matches[i][1]] += 1
        #print(d)
        #print(l)
        ans1, ans2 = [],[]

        for i in l:
            if l[i] == 0 and d[i] != 0:
                ans1.append(i)
            if l[i] == 1:
                ans2.append(i)

        ans1.sort()
        ans2.sort()
        ans = [ans1,ans2]
        return ans