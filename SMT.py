class student:
    def __init__(self,name,age,gender,dept):
        self.name = name
        self.age = age
        self.gender = gender
        self.dept = dept
    def display(self):
        print("STUDENt DETAILS")
        print("==========================================")
        print(f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}\nDepartment:{self.dept}")
        print("==========================================")
name = input("Enter The name of the student: ")
age = int(input("Enter Students Age: "))
Gender = input("Enter Students Gender: ")
Dept = input("Enter department: ")
stud = student(name,age,Gender,Dept)
stud.display()
