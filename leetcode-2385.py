# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph = {}
        #adj = self.tograph(root,None,graph)
        adj = self.tograph(root,graph)
        res = self.bfs(adj,start)
        return res

#     def tograph(self,root,parent,graph):  # create graph using DFS

#         graph[root.val] = []

#         if root.left != None:
#             graph[root.val].append(root.left.val)
#             self.tograph(root.left,root,graph)

#         if root.right != None:
#             graph[root.val].append(root.right.val)
#             self.tograph(root.right,root,graph)

#         if parent != None:
#             graph[root.val].append(parent.val)
#         return graph

    def tograph(self,root,graph): # create graph using BFS

        stack = [(root,None)]

        while(stack):
            cur, par = stack.pop(0)

            if cur and cur.val not in graph:
                graph[cur.val] = []
            if par and par.val not in graph:
                graph[par.val] = []

            if par:
                # if cur.val not in graph:
                #     graph[cur.val] = []
                # if par.val not in graph:
                #     graph[par.val] = []

                graph[cur.val].append(par.val)
                graph[par.val].append(cur.val)

            if cur.left:
                stack.append((cur.left,cur))
            if cur.right:
                stack.append((cur.right,cur))

        print(graph)
        return graph


    def bfs(self,graph,start):
        q = [start]
        #print(q)
        visit = set()
        visit.add(start)
        res = -1
        while(q):
            n = len(q)
            for i in range(n):
                t = q.pop(0)
                #print(t)
                for adjacent in graph[t]:
                    if adjacent not in visit:
                        visit.add(adjacent)
                        q.append(adjacent)
            res += 1

        return res