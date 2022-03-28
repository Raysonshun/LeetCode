class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:return 0

        stack = [(root,0)]
        d = []

        while(stack):

            cur = []
            cur_Node, cur_depth = stack.pop()
            d.append(cur_depth)

            if type(cur_Node) is Node:
                cur.append(cur_Node)
            else:
                cur = cur_Node

            for i in cur:
                if i.children:
                    stack.append((i.children,cur_depth + 1))

        m = max(d)
        return m+1