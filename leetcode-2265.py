# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(x):

            nonlocal res

            if not x:
                return (0,0)

            leftsum, leftcount = dfs(x.left)
            rightsum, rightcount = dfs(x.right)

            summ = leftsum + rightsum + x.val
            count = leftcount + rightcount + 1

            avg = summ//count

            if avg == x.val:
                res += 1

            return (summ, count)

        dfs(root)

        return res