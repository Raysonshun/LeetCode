class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stk = []
        m = defaultdict(lambda:-1)

        for i in nums2:

            while stk and stk[-1] < i:
                m[stk.pop()] = i
            stk.append(i)

        return [m[i] for i in nums1]