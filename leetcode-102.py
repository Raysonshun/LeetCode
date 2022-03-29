class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ''' My Solution
        if not root: return []

        queue = [(root,0)]

        lvl = []
        val = []

        while(queue):

            cur_Node, cur_lvl = queue.pop(0)
            val.append(cur_Node.val)
            lvl.append(cur_lvl)

            if cur_Node.left:
                queue.append((cur_Node.left,cur_lvl + 1))
            if cur_Node.right:
                queue.append((cur_Node.right,cur_lvl + 1))

        m = max(lvl)
        res = []

        for i in range(m+1):
            c = []
            for j in range(len(lvl)):
                if lvl[j] == i:
                    c.append(val[j])
            res.append(c)
        return res

        '''
        if not root: return []
        queue = [root]
        res = []
        while(queue):
            l = len(queue)
            lvl = []
            for i in range(l):
                cur_Node = queue.pop(0)
                lvl.append(cur_Node.val)
                if cur_Node.left:
                    queue.append(cur_Node.left)
                if cur_Node.right:
                    queue.append(cur_Node.right)
            res.append(lvl)
        return res