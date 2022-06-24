class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = [root]
        cur = []
        res = []
        order = 1

        while(q):

            n = len(q)

            for i in range(n):
                node = q.pop(0)
                cur.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if order == 1:
                res.append(cur)
            elif order == -1:
                cur = cur[::-1]
                res.append(cur)

            order *= -1
            cur = []

        return res