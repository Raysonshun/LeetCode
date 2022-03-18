class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0
        if not root: return 0
        self.helper(root)
        return self.maxx

    def helper(self,x):

        if not x: return 0

        l = self.helper(x.left)
        r = self.helper(x.right)

        self.maxx = max(self.maxx, l + r)
        return max(l,r) + 1