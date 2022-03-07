class Solution:

    def minimalKSum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        i = 1
        prev = nums[0]
        count = 0
        summ = 0

        if nums[0] != 1:
            start_l = nums[0] - 1
            if start_l > k:
                summ += (k+1)*k / 2
                return int(summ)
            else:
                count += start_l
                summ += (start_l + 1) * (start_l) / 2

        while(i < n):
            if nums[i]!= nums[i-1] + 1 and nums[i] != nums[i-1]:
                l = nums[i] - nums[i-1] -1
                if count + l <=k:
                    count += l
                    summ += (nums[i] + nums[i-1]) * (nums[i] - nums[i-1] + 1)/2 - nums[i] - nums[i-1]
                else:
                    l = k - count
                    count += l
                    summ += (nums[i-1] + l + nums[i-1]) * (nums[i-1] + l - nums[i-1] + 1)/2 - nums[i-1]
                if count >= k:
                    break
            i += 1

        if count < k:
            left = k - count
            l = nums[n-1] + 1
            r = nums[n-1] + left
            summ_left = (l + r) * (r - l + 1)/2
            summ = summ + summ_left

        return int(summ)


    def minimalKSum_fast(self, A: List[int], k: int) -> int:  # This is a much faster solution using binary search, see here: https://leetcode.com/problems/append-k-integers-with-minimal-sum/discuss/1823621/Python-Explanation-with-pictures

        A = sorted(list(set(A)))
        n = len(A)

        if A[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(A)

        lft, rgt = 0, n - 1
        while rgt > lft:
            mid = (lft + rgt) // 2
            if A[mid] - mid <= k:
                lft = mid + 1
            else:
                rgt = mid

        return (k + lft) * (k + lft + 1) // 2 - sum(A[:lft])
