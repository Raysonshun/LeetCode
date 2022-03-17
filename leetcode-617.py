class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        t1 = root1
        t2 = root2

        if t1 is None: return t2
        if t2 is None: return t1

        if t1 and t2:

            t2.val += t1.val

            t2.left = self.mergeTrees(t1.left,t2.left)
            t2.right = self.mergeTrees(t1.right,t2.right)

        return t2
