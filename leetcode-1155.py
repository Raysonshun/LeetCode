class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        if n*k < target or n > target:
            return 0

        path = {0:1}

        for cur_dice in range(1,n+1):
            cur_path = {}

            for value in range(1, k+1):
                for pre_sum, pre_path in path.items():
                    cur_sum = pre_sum + value
                    if cur_sum <= target:
                        cur_path[cur_sum] = cur_path.get(cur_sum,0) + pre_path

            path = cur_path

        return path[target]%(10**9+7)


    '''
DP
Let DP[i, v] represent the number of possible ways to get sum of v using i dices.
Init DP[i, v] = 0, then DP[i, v] += DP[i-1, v-n] for n in range(1, f+1), if DP[i-1, v-n] exist.
Since calculation of DP[i,v] of dice i is only based on DP[i-1, v-n], we can reuse a dict to store results for previous dice i-1
Boundary condition: {0:1}
Only count values <= target, so the size of DP dict <= target
Time: O(d x f x target)
Space: O(target)

    '''
