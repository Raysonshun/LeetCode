class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:

        import heapq as hq
        res = 1

        heap = []
        for i in nums:
            hq.heappush(heap,i)

        while(k > 0):
            temp = hq.heappop(heap)
            hq.heappush(heap,temp+1)
            k -= 1

        for i in heap:
            res = res * i
            res = res%(10**9+7) # do the modulo here, no time limit exceeded

        return res # %(10**9+7) # if do the modulo here, TLE