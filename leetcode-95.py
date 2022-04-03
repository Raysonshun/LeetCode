class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:



        def generate(start, end):

            res = []

            if start == end:
                return [TreeNode(start)]
            if start > end:
                return [None]

            for i in range(start, end + 1):

                left = generate(start, i-1)
                right = generate(i+1, end)

                for l in left:
                    for r in right:

                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r

                        res.append(cur)
            return res

        ans = generate(1,n)

        return ans