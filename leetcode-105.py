class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        rootval = preorder[0]
        root = TreeNode(preorder[0])
        indx = inorder.index(rootval)
        leftnode = self.buildTree(preorder[1:indx+1],inorder[:indx])
        rightnode = self.buildTree(preorder[indx+1:],inorder[indx+1:])
        root.left = leftnode
        root.right = rightnode
        return root