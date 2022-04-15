class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''Binary Search

        def bs(arr):

            if arr[0] >= x:
                return 0
            if arr[-1] <= x:
                return len(arr) - 1

            left = 0
            right = len(arr) - 1

            mid = (left + right) // 2

            while (left < right):


                if arr[mid] == x:
                    return mid

                elif arr[mid] <= x and arr[mid+1] > x:
                    return mid

                elif arr[mid] > x:
                    right = mid - 1

                elif arr[mid] < x:
                    left = mid + 1

                mid = (left + right)//2

            return mid

        n = len(arr)
        p = bs(arr)

        count = 0
        l, r = p,p+1

        res = []

        while (l >= 0 and r < n and count < k):

            if abs(arr[l] - x) == abs(arr[r] - x):

                res.append(arr[l])
                l -= 1
                count += 1

            elif abs(arr[l] - x) < abs(arr[r] - x):

                res.append(arr[l])
                l -= 1
                count += 1

            elif abs(arr[l] -x) > abs(arr[r] - x):

                res.append(arr[r])
                r += 1
                count += 1

        while (count < k and l >= 0):
            res.append(arr[l])
            l -= 1
            count += 1

        while (count < k and r < n):
            res.append(arr[r])
            r += 1
            count += 1

        res.sort()

        return res '''


        l,r=0,len(arr)-1
        while r-l >= k :
            if abs(x-arr[l]) <= abs(x-arr[r]) :
                r-=1
            else :
                l+=1
        return arr[l:r+1]