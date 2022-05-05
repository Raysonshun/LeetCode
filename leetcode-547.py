class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

    # DFS Solution: https://leetcode.com/problems/number-of-provinces/discuss/1134925/Python-DFS-explanation-and-comments
        N = len(isConnected)
        visited = set()

        def dfs(cityI):
            #cityIConnections is a row in isConnected, which contains the city i's connections
            cityIConnections = isConnected[cityI]
            visited.add(cityI) #add cityI to seen, so we won't dfs it again (because we called it just now!)
            #we want to take all 1's in cityIConnections to put together into a province
            for cityJ in range(N):
                #check cityJ's connections first before finishing cityI's connections
                if (cityJ not in visited) and (cityIConnections[cityJ] == 1) and (cityI != cityJ):
                    dfs(cityJ)
            #we're done searching cityI's direct connections
            return

        numProvinces = 0
        for cityI in range(N):
            #each entire dfs recursion set is going to be one province
            if cityI not in visited:
                dfs(cityI)
                numProvinces += 1
        return numProvinces

    ''' Union Find (my solution)
        n = len(isConnected)

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

        def union(x,y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i!= j:
                    union(i,j)

        # print(parent)
        # print(parent[1], find(parent[1]))

        res = set()

        for i in parent:
            res.add(find(i))

        return len(res) '''
