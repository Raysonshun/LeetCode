# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []

        def dfs(x, cur):

            if not x:
                return

            cur.append(str(x.val))

            if not x.left and not x.right:
                res.append(int(''.join(str(i) for i in cur)))
                return

            if x.left:

                dfs(x.left, cur)
                cur.pop()

            if x.right:

                dfs(x.right, cur)
                cur.pop()

        dfs(root, [])

        return sum(res)