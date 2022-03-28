class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        queue = [root]
        cur_level = 1
        nxt_level = 0

        def bfs(root):
            nonlocal cur_level
            nonlocal nxt_level

            if root:

                while(queue):

                    cur_Node = queue.pop(0)
                    cur_level -= 1
                    if cur_Node.left:
                        queue.append(cur_Node.left)
                        nxt_level += 1
                    if cur_Node.right:
                        queue.append(cur_Node.right)
                        nxt_level += 1

                    if cur_level == 0:
                        res.append((cur_Node.val))
                        cur_level = nxt_level
                        nxt_level = 0

        bfs(root)

        return res