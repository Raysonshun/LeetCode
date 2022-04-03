class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        ma = max(candies)
        n = len(candies)
        total = sum(candies)

        if total < k: return 0

        l = 1
        r = ma
        mid = (l + r)//2 # currently how many candies each child can get
        maxx = 0
        cur = 0

        while (l <= r):
            cur = 0
            for i in range(n):
                cur += candies[i]//mid

            if cur < k:
                r = mid-1
                mid = (l + r)//2
                continue

            elif cur >= k:
                maxx = max(maxx, mid)
                l = mid + 1
                mid = (l + r) //2

        return maxx