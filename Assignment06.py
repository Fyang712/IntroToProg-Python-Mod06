# ------------------------------------------------------------------------------------------ #
# Title: Assignment06.py
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   <FanYang>,<08/14/2025>,<Created Script>
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# Classes:
# •	The program includes a class named FileProcessor.
# •	The program includes a class named IO.
# •	All classes include descriptive document strings.

# Functions:
# •	All functions include descriptive document strings.
# •	All functions with except blocks include calls to the function handling error messages.
# •	All functions use the @staticmethod decorator.
# •	The program includes functions with the following names and parameters:
    # o	output_error_messages(message: str, error: Exception = None)
    # o	output_menu(menu: str)
    # o	input_menu_choice()
    # o	output_student_courses(student_data: list)
    # o	input_student_data(student_data: list)
    # o	read_data_from_file(file_name: str, student_data: list):
    # o	write_data_to_file(file_name: str, student_data: list):

# Error handling:
# •	The program provides structured error handling when the file is read into the list of dictionary rows.
# •	The program provides structured error handling when the user enters a first name.
# •	The program provides structured error handling when the user enters a last name.
# •	The program provides structured error handling when the dictionary rows are written to the file.

# Create a class to read and write data from and to the file
class FileProcessor:
    @staticmethod
    #Create function to read data from the file and add error handling messages
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    #Create function to write data to the file and add error handling messages
    def write_data_to_file(file_name: str, student_data: list):
        # global file
        # global students

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Present and Process the data using functions
class IO:
    # A collection of functions that manage user input and output
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        # This function displays a custom error messages to the user
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        # This function displays a menu of choices to the user
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        # This function gets a menu choice from the user
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        # This function displays the student and course names to the user
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        # This function gets the student's first name and last name, with a course name from the user
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}

            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

#  End of function definitions

#  Start of main script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")