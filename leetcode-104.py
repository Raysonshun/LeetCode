class Solution:
    '''   my solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        depth = 0

        def dfs(root):

            nonlocal depth

            if not root:
                return 0
            else:
                depth = max(dfs(root.left), dfs(root.right)) + 1
                return depth

        dfs(root)
        return depth
            '''

    def maxDepth(self,root):
        from collections import deque
        if not root: return 0
        depth = 0
        stack = [(root, 0)]
        while stack:
            cur_node, cur_depth = stack.pop()

            depth = max(depth, cur_depth)
            if cur_node.right:
                stack.append((cur_node.right, cur_depth+1))
            if cur_node.left:
                stack.append((cur_node.left, cur_depth+1))
        return depth+1