class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        d = {}

        for i in range(n):

            cur = strs[i]
            cur = list(cur)
            cur.sort()
            cur = ''.join(cur)

            if cur not in d:
                d[cur] = [strs[i]]
            else:
                d[cur].append(strs[i])

        res = []

        for items in d:
            temp = d[items]
            res.append(temp)

        return res