class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [(root,1)]
        s2 = []

        while(stack):

            cur_Node,cur_depth = stack.pop()
            s2.append((cur_Node.val,cur_depth))

            if cur_Node.left:
                stack.append((cur_Node.left, cur_depth + 1))
            if cur_Node.right:
                stack.append((cur_Node.right, cur_depth + 1))

        print(s2)
        m = 0

        for val, d in s2:
            if m < d:
                m = d
        res = 0
        for val, d in s2:
            if d == m:
                res += val
        return res