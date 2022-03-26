class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()


        def dfs(start,cur_sum):

            if cur_sum == target:
                res.append(path[:])
                return

            if start > len(candidates) - 1 or cur_sum > target:
                return

            i = start

            if cur_sum < target:

                while(i < len(candidates)):
                    if candidates[i] > target:
                        i += 1
                        continue
                    path.append(candidates[i])
                    dfs(i+1,cur_sum + candidates[i])
                    path.pop()
                    i += 1

                    while i < len(candidates) and candidates[i] == candidates[i-1]:
                        i += 1
                    #print(i)

        dfs(0,0)

        return res