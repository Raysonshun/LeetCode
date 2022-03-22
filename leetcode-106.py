class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder and not postorder: return None
        head = postorder[-1]


        indx = inorder.index(head)
        root = ListNode(head)
        root.left = self.buildTree(inorder[:indx], postorder[:indx])
        root.right = self.buildTree(inorder[indx+1:], postorder[indx:-1])
        return root