class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''problem can be simplified as: to find a subset with sub_sum = sum/2
           Actually a knapsack problem
           nums = weight, backpack capacity = sum/2
           No repetition
           Aim: to find if we can use items in nums to EXACTLY fulfill backpack capacity sum/2
           i: item in nums
           j: backpack capacity, from 0 - capacity
           状态ans: if we can use items in nums[0:i] to EXACTLY fulfill capacity j, True/False
           讲解：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
        '''
        '''Solution 1:
        summ = sum(nums)
        target = summ/2

        if not target.is_integer():

            return False

        target = int(target)

        n = len(nums)

        capacity = target + 1
        ans = [[False for j in range(capacity + 1)] for i in range(n+1)]
        ans[0][0] = True
        #print(ans)

        for i in range(1,n+1):
            for j in range(1,capacity + 1):
                if j < nums[i-1]:
                    ans[i][j] = ans[i-1][j]
                else:
                    p1 = ans[i-1][j] # 第i个item不加入
                    p2 = ans[i-1][j - nums[i-1]] #第j个item加入

                    if p1 or p2:
                        ans[i][j] = True

        #print(len(ans),len(ans[0]))
        return ans[n][target]
        '''
        # Solution 2" 简化为一维：
        summ = sum(nums)
        target = summ/2

        if not target.is_integer():
            return False
        target = int(target)
        n = len(nums)
        #capacity = target + 1
        ans = [True] + [False] * target
        for i,num in enumerate(nums):
            for j in range(target, num-1,-1):
                ans[j] |= ans[j-num]
        return ans[target]