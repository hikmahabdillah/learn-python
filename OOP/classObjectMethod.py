class Student:
  # name = "Hikmah"
  # classs = "TI-1F"

  # default constructor
  # def __init__(self):
  #   self.name = 'Hikmah'
  #   self.classs = "TI-1F"
  
  # parameter constructor
  def __init__(self, name, classs):
     self.name = name
     self.classs = classs

# student1 = Student()
# print(student1.name, student1.classs)

# student2 = Student()
# student2.name = "Aldrin"
# print(student2.name, student2.classs)

# student3 = Student()
# student3.name = "Eric"
# student3.classs = "TI-1D"
# print(student3.name, student3.classs)

student4 = Student("Abdillah", "TI-1F")
print(student4.name, student4.classs)