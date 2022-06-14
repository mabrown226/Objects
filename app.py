# import the classess
from school import Course, Person, Teacher, Student

teacher_list = []
student_list = []
course_list = []

def create(type):
  # first step will be to get the number of the type to create. The type will either be student or reacher. with the number to be created we can then create an array of objects to store the that type in.
  num_to_created = int(input(f'How many {type}s will you be adding: '))
  n = 0
  while n < num_to_created:
    # get name
    create_name = input(f'Input {type}s name: ')
    # get id_number 
    create_id = input(f'Input {type}s ID number: ')
    
    
    # if the type is teacher then create the object and add it to the teacher list
    if type == 'teacher':
      # create the object
      i = Teacher(create_id, create_name)
      # add the object tot the array
      teacher_list.append(i)
      n+=1
    # if the type is student then create the objet and add it to the student list
    elif type == 'student':
      # create the object
      i = Student(create_id, create_name)
      student_list.append(i)
      n+=1
    else:
      break    
    


# Function to create a course
def create_course():
  # name,course_number,total_students, teacher, student
  # ask the name of the course
  course_name = input("What is the name of the course? ")
  # ask the course number
  course_number = input("What is the course number? ")
  

  # ask the teacher name
  print('Below is a list of teacher that you can select from. Please choose the teacher that you want to select to teach the class.')
  print_names('teacher')
  temp_number = input("What is the teacher's number? ")
  for item in teacher_list:
    if item.id_number == temp_number:
      teacher = item

  # ask the total number of students
  total_students = input("How many student are in the class? ")
  print('Select the students to add to the class list.')
  print_names('student')
  

  # ask the students names
  temp_list = []
  for x in range(int(total_students)):    
    student_id = input("What is the the next student number? ")
    for item in student_list:
      if item.id_number == student_id:
        student = item
        temp_list.append(student)
        print(temp_list)
    
  
  new_class = Course(course_name, course_number, total_students, teacher, student_list)
  course_list.append(new_class)

#  funtion to print the object in a list
def print_names(type):
  if type == 'teacher':
    for item in teacher_list:
      print(item)
  elif type == 'student':
    for item in student_list:
      print(item)

# funtion to get the object from the list
def get_list_item(type, number):
  if type == 'teacher':
    for item in teacher_lister:
      if item.id_number == number:
        teacher = item
  


print('***************************************************************')
print('**                                                           **')
print('**           Create a Sample School                          **')
print('**                                                           **')
print('***************************************************************')
print('To get started we need you to answer the following questions.')
# Create a array that stores the instances of the teacher and student objects created

create('teacher')
create('student')

create_course()

for x in course_list:
  print(x)
  x.print_student()




