# Student Management System

A simple command-line Student Management System built with Python. The application allows users to add, display, search, update, and delete student records. Student data is saved locally using Python's `pickle` module.

## Features

- Display all student records
- Add a new student
- Search for a student by roll number
- Delete a student by roll number
- Update student details
- Prevent duplicate roll numbers
- Save and load student records automatically
- Store data locally in a `STUDENT.pkl` file

## Project Structure

```text
Student-Management-System---Project/
│
├── main.py           # Main menu and program entry point
├── student.py        # Student class definition
├── studmanagsys.py   # Student management operations
├── STUDENT.pkl       # Automatically generated data file
└── README.md         # Project documentation
```

## Requirements

- Python 3.10 or later

The project uses the `match` statement, which requires Python 3.10 or newer.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoelAlfred-Higgs/Student-Management-System---Project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Student-Management-System---Project
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

After starting the program, select an option from the menu:

```text
1. Display
2. Add
3. Search
4. Delete
5. Update
6. Exit
```

### Add a Student

Enter the following details:

- Student name
- Roll number
- Gender
- Department

Roll numbers must be unique.

### Search for a Student

Enter the student's roll number to view their details.

### Update a Student

Enter the roll number of the student you want to update, then select the field to modify:

1. Name
2. Roll number
3. Gender
4. Department

### Delete a Student

Enter the student's roll number to remove the record.

## Data Storage

Student records are stored in a file named `STUDENT.pkl`. The file is created automatically when the program saves data.

The data file is updated after:

- Adding a student
- Deleting a student
- Updating a student

> The `STUDENT.pkl` file contains serialized Python objects and should only be loaded from a trusted source.

## Modules

### `main.py`

Contains the command-line interface and menu system used to interact with the application.

### `student.py`

Defines the `student` class, which stores:

- Name
- Roll number
- Gender
- Department

### `studmanagsys.py`

Defines the `StudManagsys` class and contains the main operations for managing student records.

## Example

```text
1. Display
2. Add
3. Search
4. Delete
5. Update
6. Exit

Enter choice: 2
Enter Student name to be added: John Doe
Enter roll no: 101
Enter gender: Male
Enter Department: Computer Science

Student Added Successfully
```

## Future Improvements

- Add input validation for invalid entries
- Improve error handling
- Add a graphical user interface
- Replace `pickle` with a database such as SQLite
- Add automated tests
- Support sorting and filtering student records
- Add confirmation prompts before deleting records

## License

This project is intended for educational purposes.
