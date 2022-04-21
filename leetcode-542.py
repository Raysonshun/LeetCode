class Solution:

	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		m = len(mat)
		n = len(mat[0])

		for i in range(m):
			for j in range(n):
				if mat[i][j] > 0:
					top = mat[i - 1][j] if i > 0 else math.inf
					left = mat[i][j - 1] if j > 0 else math.inf
					mat[i][j] = 1 + min(top,left)


		for i in range(m - 1, -1, -1):
			for j in range(n - 1, -1, -1):
				if mat[i][j] > 0:
					bottom = mat[i + 1][j] if i < m-1 else math.inf
					right = mat[i][j + 1] if j < n-1 else math.inf
					mat[i][j] = min(mat[i][j],bottom+1,right+1)
		return mat





'''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        res = [[-1 for i in range(m)] for j in range(n)]

        count = m * n

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    count -= 1
        cur = 0

        while (count > 0):

            for i in range(n):
                for j in range(m):

                    if res[i][j] == cur:

                        if i-1 >=0 and res[i-1][j] == -1:
                            res[i-1][j] = cur + 1
                            count -= 1
                        if i+1 <= n-1 and res[i+1][j] == -1:
                            res[i+1][j] = cur + 1
                            count -= 1
                        if j-1 >= 0 and res[i][j-1] == -1:
                            res[i][j-1] = cur + 1
                            count -= 1
                        if j+1 <= m-1 and res[i][j+1] == -1:
                            res[i][j+1] = cur + 1
                            count -= 1
            cur += 1

        return res
        '''