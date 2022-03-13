class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        n1 = len(artifacts)
        n2 = len(dig)

        dig_set = set()

        for i in range(n2):
            l = dig[i][0]
            r = dig[i][1]
            temp = (l,r)
            dig_set.add(temp)

        count = 0

        for i in range(n1):
            cov = []
            rs = artifacts[i][0]
            re = artifacts[i][2]
            cs = artifacts[i][1]
            ce = artifacts[i][3]

            for r in range(rs,re+1):
                for c in range(cs,ce+1):
                    tp = (r,c)
                    cov.append((tp))
            ind = 1

            for x in range(len(cov)):
                if cov[x] not in dig_set:
                    ind  = 0
            if ind == 1:
                count += 1

        return count