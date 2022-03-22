class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:return

        temp = root.left

        if temp is not None:

            while(temp.right):
                temp = temp.right
            temp.right = root.right

            a = root.left
            root.left = None
            root.right = a

        self.flatten(root.right)
