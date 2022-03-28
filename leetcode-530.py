# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ''' My solution
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        m = float('inf')

        def maxx(root):
            cur = root
            while(cur.right):
                cur = cur.right
            return cur.val

        def minn(root):
            cur = root
            while(cur.left):
                cur = cur.left
            return cur.val

        def dfs(root):

            nonlocal m

            if not root: return

            a1, a2 = float('inf'), float('inf')

            if root.left:
                a1 = maxx(root.left)
            if root.right:
                a2 = minn(root.right)

            m = min(m, abs(a1 - root.val), abs(root.val - a2))

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return m         '''

    # Another Solution: Inorder traversal of BST always gives increasing sequence
    # so the min difference can only occur between adjacent values
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.result=sys.maxsize
        self.pre=sys.maxsize
        def helper(root):
            if root:
                helper(root.left)
                self.result=min(self.result,abs(root.val-self.pre))
                self.pre=root.val
                helper(root.right)
        helper(root)
        return self.result