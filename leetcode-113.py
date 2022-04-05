class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfs(tree,cur_sum, path):

            if not tree:
                return

            if (not tree.left) and (not tree.right):

                path.append(tree.val)
                cur_sum += tree.val
                if cur_sum == targetSum:
                    res.append(path[:])
                cur_sum -= tree.val
                path.pop()
                return

            if tree:
                path.append(tree.val)
                cur_sum += tree.val
                dfs(tree.left,cur_sum,path)
                dfs(tree.right,cur_sum,path)
                path.pop()
                cur_sum -= tree.val

        dfs(root,0,[])

        return res
