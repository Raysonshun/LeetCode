class Solution:

    def destroyTargets(self, nums: List[int], space: int) -> int:
        dct = dict()
        mx = 0

        for num in nums:
            x = num % space

            if x not in dct:
                dct[x] = (1, num)
            else:
                dct[x] = (dct[x][0] + 1, min(dct[x][1], num))

            mx = max(mx, dct[x][0])

        res = float("inf")
        for key, val in dct.items():
            if val[0] == mx:
                res = min(res, val[1])

        return res