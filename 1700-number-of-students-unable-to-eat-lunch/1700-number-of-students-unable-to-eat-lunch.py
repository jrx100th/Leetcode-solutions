class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque

        students = deque(students)
        count = 0

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.popleft()
                count = 0
            else:
                students.rotate(-1)
                count += 1

        return len(students)