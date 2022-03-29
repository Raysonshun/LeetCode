class Solution:
    def numTrees(self, n: int) -> int:

        if n <2:return 1

        trees = [0 for i in range(n+1)] # from 0 to n，tree中有i个节点时的 number of possible trees

        trees[0], trees[1], trees[2] = 1,1,2

        for i in range(3,n+1): # current max number is i

            temp = 0

            for j in range(1,i+1): # for current max as i, its root node can be 1 to i

                left_num = j - 1 # number of left subtree nodes
                right_num = i - j # number of right subtree nodes

                temp += trees[left_num] * trees[right_num]

            trees[i] = temp

        return trees[n]