# ========================================================================== 79
# FILE: Assignment05.py
#
# TITLE: Assignment 5 for UW "Foundations of Python" Course
# 
# TITLE: Assignment 5 for UW "Foundations of Python" Course
#
# DESCRIPTION: Program demonstrates the use of dictionaries, .json files, and
# exception handling in addition to the capabilities demonstrated in
# Assignment 4
#
# CHANGE LOG:
#   11/4/2025: Created by Charles Lloyd, Header, and menu/control logic and
#   adopting portions of code from the "Assignment05-Starter.py" file created
#   by R Root
#
#        1         2         3         4         5         6         7        7
# ====== 0 ======= 0 ======= 0 ======= 0 ======= 0 ======= 0 ======= 0 ====== 9
import _io
# NOTES ------ NOTES ------ NOTES ------ NOTES ------ NOTES ------ NOTES


# DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES
import json  # From Python standard library
#from io import TextIOWrapper


# CONSTANTS -- CONSTANTS -- CONSTANTS -- CONSTANTS -- CONSTANTS -- CONSTANTS
# Create the menu as a constant, using f-strings
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = 'Enrollments.json'


# VARIABLES -- VARIABLES -- VARIABLES -- VARIABLES -- VARIABLES -- VARIABLES
student_first_name: str = ''        # Entered by user
student_last_name: str = ''         # Entered by user
course_name: str = ''               # Entered by user
menu_choice: str = ''               # Selected by user
file = _io.TextIOWrapper            # type needed to use the .close() in the finally block
student_data: dict = {}             # Entered by user
students: list[dict[str, str]] = [] #
valid_resp: bool = False            # Boolean, Entered by user


# CONTROLS --- CONTROLS --- CONTROLS --- CONTROLS --- CONTROLS --- CONTROLS


# BODY ------- BODY ------- BODY ------- BODY ------- BODY ------- BODY


# Read data from file into a list of dictionaries
try:
    file = open(FILE_NAME, "r")   # Open the JSON file for reading
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("-- Technical Error Message -- ")
    print(e, e.__doc__)
    print('Data file does not exist, file will be created after saving')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    print("closing file")
    if file.closed == False:
        file.close()


# Select and perform each Menu task
while True:           # Repeat until break out using option 4
    print('\n' + MENU)
    menu_choice = input('Enter choice, 1 to 4: ')
    match menu_choice:

        case '1':   # Register a student for a course
            # Query user for input, validate, and create record
            correct = False
            while not correct:

                try:
                    student_first_name = input('\nPlease enter your FIRST name: ')
                    if not student_first_name.isalpha():
                        raise ValueError("The First name should not contain numbers.")

                    student_last_name = input('\nPlease enter your LAST name: ')
                    if not student_last_name.isalpha():
                        raise ValueError("The Last name should not contain numbers.")

                    course_name = input('\nPlease enter the COURSE name: ')
                    if not course_name[0].isalpha():
                        raise ValueError("The Course name should not begin with a number.")

                    print('First Name Entered: ' + student_first_name)
                    print('Last Name Entered: ' + student_last_name)
                    print('Course Name Entered: ' + course_name)
                    resp = input('Enter "Y" if correct, '
                                                'or any other key to re-enter: ')

                    if resp == "y" or resp == "Y":
                        correct = True

                except ValueError as e:
                    print(e)  # Prints the custom message
                    print("-- Technical Error Message -- ")
                    print(e.__doc__)
                    print(e.__str__())
                except Exception as e:
                    print("There was a non-specific error!\n")
                    print("-- Technical Error Message -- ")
                    print(e, e.__doc__, type(e), sep='\n')

    # put the strings into the student_data list
            student_data = {"name_first": student_first_name,
                            "name_last": student_last_name,
                            "name_course": course_name}

            # Combine data from multiple students (list of dictionaries)
            students.append(student_data)

        case '2':   # Show current data
            if students:
                print('Student registration data:')
                for student_data in students:
                    print(f'{student_data["name_first"]},{student_data["name_last"]},'
                          f'{student_data["name_course"]}')
                print('\n')
                for student_data in students:
                    print(f'{student_data["name_first"]} {student_data["name_last"]} '
                          f'is registered for {student_data["name_course"]}')
            else:
                print('No data have been entered yet')

        case '3':   # Save data to a .json file
            if students:
                try:
                    file = open(FILE_NAME, 'w')
                    json.dump(students, file, indent=2)
                    print('Saved the record to file')
                    for row in students:
                        print(row)
                except Exception as e:
                    print("There was a non-specific error!\n")
                    print("-- Technical Error Message -- ")
                    print(e, e.__doc__, type(e), sep='\n')
                finally:
                    if file.closed == False:
                        file.close()
            else:
                print('You must have data for at least one student before '
                                                            'saving to file')


        case '4':   # Exit the program
            # Inform user and Exit the program
            print('Exited the program')
            break

        case _:   # Handle invalid menu choices
            print('Invalid Menu Choice')
            continue
