class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        res = ['' for i in s]

        self.parent = [i for i in range(len(s))]

        for a,b in pairs:

            self.union(a,b)

        d = {}

        for ind,c in enumerate(s):

            l = self.find(ind)
            if l not in d:
                d[l] = ([c],[ind])
            else:
                d[l][0].append(c)
                d[l][1].append(ind)

        for swapchar, swapindx in d.values():

            swapchar.sort()
            swapindx.sort()

            for ch, idx in zip(swapchar,swapindx):
                res[idx] = ch

        res = ''.join(res)

        return res

    def union(self,a,b):

        self.parent[self.find(a)] = self.find(b)

    def find(self,a):

        if self.parent[a] == a:
            return a

        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]