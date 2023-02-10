from roster import student_roster
import itertools
student_roster_iterator = iter(student_roster)

try:
    while True:
        student = next(student_roster_iterator)
        print(student)
except StopIteration:
    pass

            
class ClassroomOrganizer:
    def __init__(self, student_roster):
        self.student_roster = sorted(student_roster, key=lambda x: x['first_name'])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.student_roster):
            student = self.student_roster[self.index]
            self.index += 1
            return student['first_name'] + ' ' + student['last_name']
        else:
            raise StopIteration
        
    def table_combinations(self):
        return list(itertools.combinations(self.student_roster, 2))
    
    def get_students_with_subject(self, subject):
        return (student for student in self.student_roster if subject in student['favorite_subjects'])
    
    def print_roster(self):
        for student in self.student_roster:
            print(student)

classroom = ClassroomOrganizer(student_roster)
math_students = list(classroom.get_students_with_subject("Math"))
science_students = list(classroom.get_students_with_subject("Science"))
math_and_science_students = [student for student in math_students if student in science_students]

combinations = list(itertools.combinations(math_and_science_students, 4))

print("Combinations of 4 students with Math and Science as favorite subjects:")
for combination in combinations:
    print(combination)

print("Table Combinations:")
for table in classroom.table_combinations():
    print(table)

try:
    while True:
        student = next(classroom)
        print(student)
except StopIteration:
    pass

for student in classroom:
    print(student)
    