class Solution:

    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        if root.left is not None and root.left.left is None and root.left.right is None:

            self.res += root.left.val

        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)

        return self.res


        def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        if root:
            # the next one on the left is a left leave
            if root.left and root.left.left == None and root.left.right == None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)
            total += self.sumOfLeftLeaves(root.right)
        return total