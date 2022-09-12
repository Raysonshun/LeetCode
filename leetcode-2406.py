class Solution:
	def minGroups(self, intervals: List[List[int]]) -> int:

		intervals.sort()

		minHeap = []

		for left, right in intervals:

			if minHeap and left > minHeap[0]:
				heapq.heappop(minHeap)

			heapq.heappush(minHeap, right)

		return len(minHeap)


        #explanation: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/2560020/Min-Heap