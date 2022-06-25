class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # DFS

        visit = [0 for i in range(n)]
        d = {}
        for i in range(n):
            d[i] = []

        for i,j in edges:   # record the connected points for each point in n
            d[i].append(j)
            d[j].append(i)

        #print(d)
        def dfs(x):

            if visit[x] == 1:
                return 0

            visit[x] = 1
            val = 1  # point is connected at least with itself

            for i in d[x]:
                val += dfs(i)    # how many points in current circle
            return val

        circle = []
        for i in range(n):
            if visit[i] == 0:
                circle.append(dfs(i)) # record different circles, and # of points in each circle
        print(circle)
        res = n*(n-1)//2 # total number of possible connected pairs

        for i in circle:
            res -= i*(i-1)//2
        return res


        ''' Union Find'''
#         self.parent = [i for i in range(n)]
#         d = {}
#         temp = []
#         for a,b in edges:
#             self.union(a,b)

#         for i in range(n):
#             x = self.find(i)
#             self.parent[i] = x

#         for i in range(n):
#             root = self.parent[i]

#             if root not in d:
#                 d[root] = [i]
#             else:
#                 d[root].append(i)


#         for i in d:
#             l = len(d[i])
#             temp.append(l)

#         res = 0
#         cur = temp[0]

#         for i in range(1,len(temp)):
#             res += cur * temp[i]
#             cur += temp[i]

#         return res

#     def union(self,a,b):
#         self.parent[self.find(a)] = self.find(b)

#     def find(self,a):

#         if self.parent[a] == a:
#             return a
#         else:
#             self.parent[a] = self.find(self.parent[a])
#             return self.parent[a]

#https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/discuss/2195871/python-union-find


