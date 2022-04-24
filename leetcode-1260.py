class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        res = [x[:] for x in grid]
        #print(grid)

        while(k):

            grid = [x[:] for x in res]

            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):

                    #print(grid,i,j)

                    if i == m-1 and j == n-1 :
                        res[0][0] = grid[i][j]
                        continue
                    elif j == n-1:
                        res[i+1][0] = grid[i][j]
                        continue
                    else:
                        res[i][j+1] = grid[i][j]
                        continue

            k -= 1

        return res