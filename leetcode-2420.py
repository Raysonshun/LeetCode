class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ### forward pass.
        forward = [False]*len(nums) ### For the forward pass, store if index i is good or not.
        stack = []
        for i in range(len(nums)):
        	### if the leangth of stack is greater or equal to k, it means this index is good.
            if len(stack)>=k:
                forward[i] = True
            ### if the stack is empty, just add the current number to it.
            if not stack:
                stack.append(nums[i])
            ### check to see if the current number is smaller or equal to the last number in stack, if it is not, put this number into the stack.
            else:
                if nums[i]<=stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]
        ### backward pass
        res = []
        stack = []
        for i in reversed(range(len(nums))):
        	### Check to see if the length of stack is greater or equal to k and also check if the forward pass at this index is Ture.
            if len(stack)>=k and forward[i]:
                res.append(i)
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i]<=stack[-1]:
                    stack.append(nums[i])
                else:
                    stack = [nums[i]]
        return res[::-1]

    ## explanation: https://leetcode.com/problems/find-all-good-indices/discuss/2620637/Python3-Two-passes-O(n)-with-line-by-line-comments.