class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        visited = [[False] * n for i in range(m)]

        def dfs(x, y):

            if visited[x][y]:
                return

            visited[x][y] = True

            for newx, newy in [(x-1, y), (x+1,y), (x, y-1), (x, y+1)]:

                if newx < 0 or newx > m-1 or newy < 0 or newy > n-1 or grid[newx][newy] == '0':
                    continue

                dfs(newx, newy)

        res = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1' and not visited[i][j]:
                    #print(i,j)
                    dfs(i,j)
                    res += 1

        return res