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