class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        n = len(rectangles)
        rectangles = sorted(rectangles, key = lambda x:x[0])

        d = {}

        for i in rectangles:
            if i[1] not in d:
                d[i[1]] = [i[0]]
            else:
                d[i[1]].append(i[0])

        def include(x,y):

            count = 0

            for h, l in d.items():
                if h >= y:
                    count += len(l) - bisect_left(l,x)
            return count

        res = []

        for i in points:

            c = include(i[0],i[1])

            res.append(c)

        return res