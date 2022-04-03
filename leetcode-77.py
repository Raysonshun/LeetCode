class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        r = [i for i in range(1,n+1)]
        print(r)

        def backtrack(cur, cur_l, start):

            if cur_l == k:
                res.append(cur[:])
                return

            if cur_l > k:
                return

            for i in range(start,n+1):
                cur.append(r[i-1])
                backtrack(cur,cur_l + 1,r[i-1] + 1)
                cur.pop()

        backtrack([],0, 1)
        return res