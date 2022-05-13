class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        l = 0
        c = 0    # count how many nodes we need to subtract from the last level

        temp = root
        d = 0   # depth of tree

        while(temp):
            d += 1
            temp = temp.left

        def dfs(x, level):
            nonlocal c
            nonlocal d

            if not x:
                return

            ri = dfs(x.right, level + 1)
            le = dfs(x.left, level + 1)

            if not ri and level == d-1:     # count how many nodes we need to subtract from the last level
                c += 1

            if not le and level == d-1:   # count how many nodes we need to subtract from the last level
                c += 1

            return 1

        dfs(root,1)

        res = 0

        for i in range(d-1):
            res += 2**(i)
        res += 2**(d-1) - c

        return res