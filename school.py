class Course():
  def __init__(self,name,course_number,total_students, teacher, student):
    self.name = name
    self.course_number = course_number
    self.total_students = total_students
    self.teacher = teacher
    self.student = student

  def __repr__(self):
    return f"""Course Name: {self.name} 
               Course Number {self.course_number} 
               Teacher: {self.teacher.name}
               Students: {self.student[0].name}"""

  def print_student(self):
    for x in self.student:
      print(x.name)

class Person():
  def __init__(self, id_number, name):
    self.id_number = id_number
    self.name = name
    

  def __repr__(self):
    return f"Person: {self.name} | ID number: {self.id_number}"

class Teacher(Person):
  def __init__(self, id_number, name):
    Person.__init__(self, id_number, name)
    

  def __str__(self):
    return f"Teacher: {self.name} | ID Number: {self.id_number}"
  

class Student(Person):
  def __init__(self, id_number, name):
    Person.__init__(self, id_number, name)
   

  def __str__(self):
    return f"Stundent: {self.name} | ID Number: {self.id_number}"

  




