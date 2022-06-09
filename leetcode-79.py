class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        directions = [(-1,0), (0,-1), (0,1),(1,0)]
        visit = [[0 for i in range(n)] for j in range(m)]

        def dfs(x,y,cur):

            if cur == '':
                return True

            for dx, dy in directions:

                nextx = x + dx
                nexty = y + dy

                if 0<=nextx<m and 0<=nexty<n and board[nextx][nexty] == cur[0] and visit[nextx][nexty] == 0:

                    visit[nextx][nexty] = 1

                    if dfs(nextx, nexty, cur[1:]):
                        return True

                    visit[nextx][nexty] = 0

            return False

        for i in range(m):
            for j in range(n):

                if board[i][j] == word[0]:

                    visit[i][j] = 1

                    if dfs(i,j,word[1:]):
                        return True

                    visit[i][j] = 0

        return False