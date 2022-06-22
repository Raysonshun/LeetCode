class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []

        q = [root]
        cur = []

        while(q):

            n = len(q)

            for i in range(n):
                cur.append(q.pop(0))

            for i in cur:
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)

            temp = cur[0].val

            for i in cur:
                if i.val > temp:
                    temp = i.val

            cur = []

            res.append(temp)

        return res