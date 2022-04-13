class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        h = []

        row = len(matrix)
        column = len(matrix[0])
        ind = 0

        for i in range(row):

            for j in range(column):

                if len(h) < k:
                    heappush(h,(-matrix[i][j]))

                elif (-h[0]) < matrix[i][j]:
                        ind = 1
                        break

                else:
                    heappop(h)
                    heappush(h,-matrix[i][j])

        h = [-i for i in h]
        h.sort()

        return h[-1]