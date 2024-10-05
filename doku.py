class Student:
    
    def __init__(self, name, reg_number, course, year):
      self.name = name
      self.reg_number = reg_number
      self.course = course
      self.year = year

    def display_reg_number(self):
      print(f"Name: {self.name}")
      print(f"Reg_number: {self.reg_number}")
      print(f"Course: {self.course}")
      print(f"Year: {self.year}")

student1 = Student('John Paul', '2500', 'BSIT', 'Two')
student1.display_reg_number()

student2 = Student('Emmanuel Duku', '2501', 'BSCS', 'Three')
student2.display_reg_number()

student3 = Student('Charity Chandia', '2502', 'BSIT', 'One')
student3.display_reg_number()
