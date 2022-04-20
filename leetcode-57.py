class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        intervals.append(newInterval)

        intervals.sort(key=lambda x: x[0])

        cur = intervals[0]

        for i in intervals:

            if i[0] > cur[1]:
                res.append(cur)
                cur = i
            else:
                cur = [min(i[0], cur[0]), max(i[1], cur[1])]

        res.append(cur)
        return res