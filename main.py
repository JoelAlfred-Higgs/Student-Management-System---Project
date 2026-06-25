from studmanagsys import StudManagsys
try:
 lis1 = StudManagsys()
 lis1.save()
 while True:
    while True:
     print("\n1. Display")
     print("2. Add")
     print("3. Search")
     print("4. Delete")
     print("5. Update")
     print("6. Exit")

     choice = int(input("Enter choice: "))
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
