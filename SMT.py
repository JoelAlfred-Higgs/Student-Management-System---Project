class student:
    def __init__(self,name,roll,gender,dept):
        self.name = name
        self.roll = roll
        self.gender = gender
        self.dept = dept
    def display(self):
        print("STUDENT DETAILS")
        print("==========================================")
        print(f"Name:{self.name}\nRoll:{self.roll}\nGender:{self.gender}\nDepartment:{self.dept}")
        print("==========================================")
    def add(self,Nname,Nroll,Ngen,Ndept):
        stud = student(Nname,Nroll,Ngen,Ndept)
        ls.append(stud)
    def search(self,searcroll):
     found = False
     for i in ls:
         if searcroll == i.roll:
            found = True
            print("=========================================")
            print(f"Name:{i.name}\nRoll:{i.roll}\nGender:{i.gender}\nDepartment:{i.dept}")
            print("=========================================")
            break
     if not found:
        print("Student Details Not Found")
    def delete(self,delroll):
        deldet = stud.search(delroll)
        del deldet
ls = []
name = input("Enter The name of the student: ")
roll = int(input("Enter Students Roll.no: "))
Gender = input("Enter Students Gender: ")
Dept = input("Enter department: ")
stud = student(name,roll,Gender,Dept)
ls.append(stud)
while True:
    choice = int(input("Enter Operation number(1-display,2-add,3-search,4-delete):"))
    match choice:
        case 1:
            for i in ls:
                i.display()
        case 2:
            Nname = input("Enter Student name to be added: ")
            Nroll = int(input("Enter roll no: "))
            Ngen = input("Enter gender: ")
            Ndept = input("Enter Department: ")
            stud.add(Nname,Nroll,Ngen,Ndept)
        case 3:
            searcroll = int(input("Enter students rollNo: "))
            stud.search(searcroll)
        case 4:
            delroll = int(input("Enter student roll no to be deleted:"))
            stud.delete(delroll)
        case _:
            print("Invalid Choice")
    ch = input("Do you wish to continue (y/n): ")
    if ch.lower() != 'y':
        break
 
    
        


