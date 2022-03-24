class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []

        def backtrack(start, cur):

            if cur == target:
                res.append(path[:])
                return

            if cur < target:
                for i in range(start,len(candidates)):
                    path.append(candidates[i])
                    backtrack(i,cur + candidates[i])
                    path.pop()

        backtrack(0, 0)

        return res