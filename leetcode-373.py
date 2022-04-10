class Solution:
    # my solution
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        '''Initial Solution - SLOW
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
        '''



        # fast solution

        import heapq as hq
        res = []
        heap = []

        for i in range(min(len(nums1),k)):
            hq.heappush(heap, (nums1[i] + nums2[0], i,0))

        while(k > 0 and heap):
            s,i1,i2 = hq.heappop(heap)
            res.append([nums1[i1], nums2[i2]])
            k -= 1
            i2 += 1

            if i1 < len(nums1) and i2 < len(nums2):
                hq.heappush(heap,(nums1[i1] + nums2[i2], i1, i2))

        return res



    #def kSmallestPairs(self, nums1, nums2, k):
        # """
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :type k: int
        # :rtype: List[List[int]]
        # """
        # if len(nums1)==0 or len(nums2)==0:
        #     return []
        # q=[]
        # for i in range(min([len(nums1),k])):
        #     heapq.heappush(q, (nums1[i]+nums2[0], (i,0)))
        # ret=[]
        # while len(ret)<k and len(q)>0:
        #     cur=heapq.heappop(q)
        #     ret.append([nums1[cur[1][0]],nums2[cur[1][1]]])
        #     if cur[1][1]+1<min([len(nums2),k]):
        #         heapq.heappush(q, (nums1[cur[1][0]]+nums2[cur[1][1]+1], (cur[1][0],cur[1][1]+1)))
        # return ret

