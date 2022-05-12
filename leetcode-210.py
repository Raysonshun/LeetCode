class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        parent, pre = {}, {}

        for course, preq in prerequisites:

            if preq not in parent:
                parent[preq] = [course]
            else:
                parent[preq].append(course)

            if course not in pre:
                pre[course] = 1
            else:
                pre[course] += 1

        res = []
        q = []

        for i in range(numCourses):
            if i not in pre: # course i only serve as parent, no prerequisite course for i
                q.append(i)
                res.append(i)

        while (q):

            c = q.pop(0)
            numCourses -= 1

            if c in parent:

                for course in parent[c]:

                    pre[course] -= 1

                    if pre[course] == 0:
                        q.append(course)
                        res.append(course)


        if numCourses != 0:
            return []
        else:
            return res