# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(x):

            if not x or x == p or x == q:
                return x

            l = dfs(x.left)
            r = dfs(x.right)

            if l and r:
                return x
            elif (l and not r):
                return l
            elif (not l and r):
                return r

        return dfs(root)