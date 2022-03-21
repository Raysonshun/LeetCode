# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.res = []
        path = ""   # cannot use self. here
        self.dfs(root,path)
        return self.res



    def dfs(self,cur,path):
        if not cur: return

        if not cur.left and not cur.right:  # leaf node

            self.res.append(path + str(cur.val))
            return

        self.dfs(cur.left,path + str(cur.val) + '->')
        self.dfs(cur.right,path + str(cur.val) + '->')
