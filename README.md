# Student Management System

A simple yet effective Student Management System built with Python that allows you to manage student records efficiently.

## 📋 Project Overview

This Student Management System is a command-line application designed to help educational institutions manage student data. It provides core functionality for adding, searching, displaying, and deleting student records with a user-friendly menu-driven interface.

## ✨ Features

- **Add Students**: Add new student records with name, roll number, gender, and department information
- **Display Students**: View details of all students currently in the system
- **Search Students**: Search for a specific student using their roll number
- **Delete Students**: Remove student records from the system by roll number
- **Error Handling**: Robust error handling for invalid inputs and data validation

## 🏗️ System Architecture

### Classes

#### 1. `student`
Represents an individual student with the following attributes:
- `name`: Student's full name
- `roll`: Student's roll number (unique identifier)
- `gender`: Student's gender
- `dept`: Student's department

**Methods:**
- `display()`: Prints the student's details in a formatted manner

#### 2. `StudManagsys`
Manages the collection of students and provides operations for managing the student list.

**Methods:**
- `add(Nname, Nroll, Ngen, Ndept)`: Adds a new student to the system
- `search(searcroll)`: Searches for a student by roll number
- `delete(delroll)`: Removes a student by roll number

## 🚀 How to Run

1. Ensure Python 3.10+ is installed (project uses match-case statements)
2. Run the program:
   ```bash
   python SMT.py
   ```

3. Follow the on-screen prompts to interact with the system

## 💻 Usage Instructions

### Initial Setup
When you first run the program, you'll be prompted to enter initial student details:
- Student name
- Roll number
- Gender
- Department

### Main Menu Operations
The system presents you with the following options:

**Option 1 - Display**: Shows all student records currently stored in the system
```
Enter Operation number(1-display,2-add,3-search,4-delete): 1
```

**Option 2 - Add**: Add a new student to the system
```
Enter Operation number(1-display,2-add,3-search,4-delete): 2
```

**Option 3 - Search**: Find a student by their roll number
```
Enter Operation number(1-display,2-add,3-search,4-delete): 3
```

**Option 4 - Delete**: Remove a student by their roll number
```
Enter Operation number(1-display,2-add,3-search,4-delete): 4
```

**Continue or Exit**: After each operation, you're asked if you want to continue (y/n)

## 📝 Input Requirements

- **Name**: Text input (string)
- **Roll Number**: Numeric input (integer)
- **Gender**: Text input (string) - e.g., "Male", "Female"
- **Department**: Text input (string) - e.g., "CSE", "ECE", "Mechanical"

## ⚠️ Error Handling

The program includes error handling for:
- Invalid menu choices
- Type conversion errors (e.g., non-numeric roll number input)
- Data validation

Invalid inputs are caught with a `ValueError` exception that displays an error message and prompts the user to re-enter data.

## 🔧 Technical Details

- **Language**: Python 3.10+
- **Programming Paradigm**: Object-Oriented Programming (OOP)
- **Data Structure**: List to store student objects
- **Control Flow**: Match-case statement for menu selection

## 📌 Example Workflow

```
1. Start the program
2. Enter initial student: John Doe, 101, Male, CSE
3. Display all students (Option 1)
4. Add more students (Option 2)
5. Search for a student (Option 3)
6. Delete a student (Option 4)
7. Continue or exit based on user choice
```

## 🐛 Known Limitations

- Data is not persisted - student records are lost when the program exits
- Single instance management - can only work with one student list at a time
- No duplicate prevention for roll numbers

## 🚧 Future Enhancements

- File-based or database persistence
- Duplicate roll number validation
- Advanced search filters (by name, department, etc.)
- Data export functionality (CSV, Excel)
- User authentication and role management
- Graphical User Interface (GUI)

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author

Created by: JoelAlfred-Higgs

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

---

**Last Updated**: June 2026
