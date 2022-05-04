class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # https://leetcode.com/problems/rotting-oranges/discuss/1992344/Python-BFS-solution

        m, n = len(grid), len(grid[0])

        t = -1

        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))

        while(q):
            l = len(q)

            for i in range(l):
                badx,bady = q.pop(0)

                directions = [(0,1), (0,-1),(-1,0),(1,0)]

                for dx, dy in directions:
                    adjx = badx + dx
                    adjy = bady + dy
                    if 0<=adjx<m and 0<=adjy<n and grid[adjx][adjy] == 1:
                        grid[adjx][adjy] = 2
                        q.append((adjx,adjy))
            t += 1



        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        if t == -1:
            return 0
        else:
            return t