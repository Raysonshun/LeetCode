class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_pre = {}
        parent = {} #以course i为prerequisite的课list/完成第i课之后可以上哪些课

        for course, pre in prerequisites:

            if pre not in parent:
                parent[pre] = [course]
            else:
                parent[pre].append(course)

            if course not in course_pre:
                course_pre[course] = 1
            else:
                course_pre[course] += 1

        q = []

        for course in range(numCourses): #可以直接完成而没有prerequisite的课

            if course not in course_pre:
                q.append(course)

        while(q):

            course = q.pop(0)
            #print(course)
            numCourses -= 1

            if course in parent:
                for childs in parent[course]:
                    course_pre[childs] -= 1
                    if course_pre[childs] == 0:
                        q.append(childs)

        return numCourses == 0
        # https://leetcode.com/problems/course-schedule/discuss/229898/Python-BFS-beats-100-with-explanation