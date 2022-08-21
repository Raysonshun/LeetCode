class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        graph = {}
        adj = self.tograph(root,None,graph)
        res = self.bfs(adj,start)
        return res

    def tograph(self,root,parent,graph):

        graph[root.val] = []

        if root.left != None:
            graph[root.val].append(root.left.val)
            self.tograph(root.left,root,graph)

        if root.right != None:
            graph[root.val].append(root.right.val)
            self.tograph(root.right,root,graph)

        if parent != None:
            graph[root.val].append(parent.val)
        return graph

    def bfs(self,graph,start):
        q = [start]
        visit = set()
        visit.add(start)
        res = -1
        while(q):
            n = len(q)
            for i in range(n):
                t = q.pop(0)
                for adjacent in graph[t]:
                    if adjacent not in visit:
                        visit.add(adjacent)
                        q.append(adjacent)
            res += 1

        return res