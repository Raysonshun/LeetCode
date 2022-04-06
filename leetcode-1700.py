class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        n = len(students)
        cur_l = n
        count = 0

        while(sandwiches):

            if count == cur_l:
                break

            if students[0] == sandwiches[0]:
                count = 0
                students.pop(0)
                sandwiches.pop(0)
                continue

            else:

                cur_l = len(students)
                temp = students.pop(0)
                students.append(temp)
                count += 1

        return len(students)