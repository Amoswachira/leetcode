class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                #if only students of one preference are left
                #and that preference sandwich present is not there
                #then infinite loop will occur hence break
                if len(set(students)) == 1 and students[0] != sandwiches[0]:
                    break
        return len(students)
        