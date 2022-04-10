class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        import heapq as hq

        res = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if len(res) < k:
                    hq.heappush(res,( - (nums1[i] + nums2[j]),[nums1[i],nums2[j]]))

                else:
                    t = hq.heappop(res)
                    t1 = t[0]
                    if (-t1) <= nums1[i] + nums2[j]:
                        hq.heappush(res,t)
                        break
                    else:
                        hq.heappush(res,(- (nums1[i] + nums2[j]),[nums1[i],nums2[j]]))

        ans = [res[i][1] for i in range(len(res))]

        return ans
