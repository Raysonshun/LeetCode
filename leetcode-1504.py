import math
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m = len(mat)
        n = len(mat[0])

        rowsum = [[0]*n for i in range(m)]

        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
                    rowsum[i][j] = count    #rowsum 用来统计每一行为底边，到第j个元素为底角的单行矩阵个数
                else:
                    count = 0

        res = 0

        for i in range(m):
            for j in range(n):

                if mat[i][j] == 1:

                    cur = math.inf

                    for k in range(i, -1,-1):      # 向上统计以i,j为右下角的矩阵个数

                        if rowsum[k][j] == 0:
                            break
                        cur = min(cur, rowsum[k][j])

                        res += cur

        return res



        # https://leetcode-cn.com/problems/count-submatrices-with-all-ones/solution/tong-ji-quan-1-zi-ju-xing-by-leetcode-solution/