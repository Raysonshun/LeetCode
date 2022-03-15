class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self,root:Optional[TreeNode]) -> List[int]:


        cur = root
        stk = []
        res = []

        while True:

            if cur is not None:
                stk.append(cur)
                cur = cur.left

            elif(stk):
                cur = stk.pop()
                res.append(cur.val)
                cur = cur.right

            else:
                break

        return res