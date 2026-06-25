import pickle as p
import os
try:
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
 
 class StudManagsys:   
    def __init__(self):
       self.ls = []  
       if os.path.exists("STUDENT.pkl"):
          try:
             with open("STUDENT.pkl","rb") as f:
                self.ls = p.load(f)
          except EOFError:
             self.ls = []
             
    def add(self,Nname,Nroll,Ngen,Ndept):
      for i in self.ls:
        if i.roll == Nroll:
            print("Roll Number Already Exists!")
            return

      stud = student(Nname,Nroll,Ngen,Ndept)
      self.ls.append(stud)
      print("Student Added Successfully")

    def search(self,searcroll):
     found = False
     for i in self.ls:
         if searcroll == i.roll:
            found = True
            print("=========================================")
            print(f"Name:{i.name}\nRoll:{i.roll}\nGender:{i.gender}\nDepartment:{i.dept}")
            print("=========================================")
            break
     if not found:
        print("Student Details Not Found")
        
    def delete(self, delroll):
     found = False
     for i in self.ls:
        if i.roll == delroll:
            self.ls.remove(i)
            found = True
            print("Student Deleted Successfully")
            break
     if not found:
        print("Student Not Found")

    def update(self,roll):
       ch = int(input("Enter Detail you want to update(1-name,2-roll,3-gender,4-department:)"))
       f = False
       for i in self.ls:
          if i.roll == roll:
             f = True
             match(ch):
                case 1:
                   n = input("Enter new name to update: ")
                   i.name = n
                case 2:
                   for s in self.ls:
                      r = int(input("Enter new roll.no to be updated: "))

                      for s in self.ls:
                        if s.roll == r:
                           print("Roll already exists")
                           return

                        i.roll = r
                        print("Roll updated successfully")
                case 3:
                   g = input("Enter gender to update: ")
                   i.gender = g
                case 4:
                   d = input("Enter new dept to update: ")
                   i.dept = d
                case _ :
                   print("Incorrect input! Data does not exist to update")
       if not f:
          print("Student not found!")
    def save(self):
       with open("STUDENT.pkl","wb") as f:
          p.dump(self.ls,f) 
   
 lis1 = StudManagsys()
 lis1.save()

 while True:
    choice = int(input("Enter Operation number(1-display,2-add,3-search,4-delete,5-Update):"))
    
    match choice:
        case 1:
            for i in lis1.ls:
                i.display()
        
        case 2:
            Nname = input("Enter Student name to be added: ")
            Nroll = int(input("Enter roll no: "))
            Ngen = input("Enter gender: ")
            Ndept = input("Enter Department: ")
            lis1.add(Nname,Nroll,Ngen,Ndept)
            lis1.save()
        
        case 3:
            searcroll = int(input("Enter students rollNo: "))
            lis1.search(searcroll)
         
        
        case 4:
            delroll = int(input("Enter student roll no to be deleted:"))
            lis1.delete(delroll)
            lis1.save()

        case 5:
             roll = int(input("Enter student roll.no: "))
             lis1.update(roll)
             lis1.save()
        
        case _:
            print("Invalid Choice")
    ch = input("Do you wish to continue (y/n): ")
    
    if ch.lower() != 'y':
        break
except Exception as e:
    print("Unexpected Error:", e)



    
        


