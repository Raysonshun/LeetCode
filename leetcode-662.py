class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        a=[(root,0)]
        max_width=0

        while a:

            n=len(a)

            for i in range(n):

                node,curr=a.pop(0)

                if i==0:
                    start=curr
                if i==n-1:
                     end=curr

                if node.left:
                    a.append((node.left,2*curr+1))

                if node.right:
                    a.append((node.right,2*curr+2))

            max_width=max(max_width,end-start+1)

        return max_width