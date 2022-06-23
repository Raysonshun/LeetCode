# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        value = []

        q = [root]

        while q:

            cur = q.pop(0)

            value.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        heapify(value)

        res = []

        for i in range(k):
            res.append(heappop(value))

        return res[-1]