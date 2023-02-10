def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }
 
def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])