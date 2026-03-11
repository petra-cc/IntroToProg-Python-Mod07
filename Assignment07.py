# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created Script
#   Petra Chinsangaram, 3/10/2026, Added Person and Student data classes
# ------------------------------------------------------------------------------------------ #
import json
import _io

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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Data classes
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    - Petra Chinsangaram, 3.10.2026: Created the class.
    """

    # Constructor
    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        This function creates a new person object.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param first_name: The person's first name.
        :param last_name: The person's last name.

        :return: None
        """
        self.first_name = first_name
        self.last_name = last_name

    # First name getter
    @property
    def first_name(self):
        """
        This function returns the person's first name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: The person's first name.
        """
        return self._first_name.title

    # First name setter
    @first_name.setter
    def first_name(self, value: str):
        """
        This function sets the person's first name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param value: String entered by the user.

        :return: None
        """
        if value.isalpha() or value == "":
            self._first_name = value
        else:
            raise ValueError("The first name should contain only letters.")

    # Last name getter
    @property
    def last_name(self):
        """
        This function returns the person's last name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: The person's last name.
        """
        return self._last_name.title

    # Last name setter
    @last_name.setter
    def last_name(self, value: str):
        """
        This function sets the person's last name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param value: String entered by the user.

        :return: None
        """
        if value.isalpha() or value == "":
            self._last_name = value
        else:
            raise ValueError("The last name should contain only letters.")

    # Override __str__ method
    def __str__(self):
        """
        This function overrides the __str__ method to return a string representation of the person.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: Comma-separated string containing the person's first and last name.
        """
        return f"{self.first_name},{self.last_name}"


class Student(Person):
    """
    A child of the Person class representing student data.

    Properties:
    - student_first_name (str): The student's first name.
    - student_last_name (str): The student's last name.
    - course_name (str): The name of the course.

    ChangeLog:
    - Petra Chinsangaram, 3.10.2026, Created the class.
    """

    # Constructor
    def __init__(self, student_first_name: str = "",
                 student_last_name: str = "", course_name: str = ""):
        """
        This function creates a new student object.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param student_first_name: The student's first name.
        :param student_last_name: The student's last name.
        :param course_name: The name of the course.

        :return: None
        """
        super().__init__(first_name=student_first_name,
                         last_name=student_last_name)
        self.course_name = course_name

    # Student first name getter
    @property
    def student_first_name(self):
        """
        This function returns the student's first name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: The student's first name.
        """
        return self._first_name.title

    # Student first name setter
    @student_first_name.setter
    def student_first_name(self, value: str):
        """
        This function sets the student's first name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param value: String entered by the user.

        :return: None
        """
        if value.isalpha() or value == "":
            self._first_name = value
        else:
            raise ValueError("The first name should contain only letters.")

    # Student last name getter
    @property
    def student_last_name(self):
        """
        This function returns the student's last name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: The student's last name.
        """
        return self._last_name.title

    # Student last name setter
    @student_last_name.setter
    def student_last_name(self, value: str):
        """
        This function sets the student's last name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param value: String entered by the user.

        :return: None
        """
        if value.isalpha() or value == "":
            self._last_name = value
        else:
            raise ValueError("The last name should contain only letters.")

    # Course name getter
    @property
    def course_name(self):
        """
        This function returns the course name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: The name of the course.
        """
        return self._course_name.title

    # Course name setter
    @course_name.setter
    def course_name(self, value: str):
        """
        This function sets the course name.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :param value: String entered by the user.

        :return: None
        """
        self._course_name = value

    # Override __str__ method
    def __str__(self):
        """
        This function overrides the __str__ method to return a string representation of the student.

        ChangeLog: (Who, When, What)
        Petra Chinsangaram,3.10.2026,Created function

        :return: Comma-separated string containing the student's first and last name and course name.
        """
        return (f"{self.student_first_name},"
                f"{self.student_last_name},{self.course_name}")


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Petra Chinsangaram,3.10.2026,Updated to convert json data to list of Student objects

        :param file_name: string data with name of file to read from.
        :param student_data: list of Student objects.

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            for student in json_students:
                student_object: Student = Student(student_first_name=
                                                  student["FirstName"],
                                                  student_last_name=
                                                  student["LastName"],
                                                  course_name=
                                                  student["CourseName"])
                student_data.append(student_object)
            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem"
                                             "with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Petra Chinsangaram,3.10.2026,Updated to convert Student objects to dictionaries

        :param file_name: string data with name of file to write to.
        :param student_data: list of dictionary rows to be writen to the file.

        :return: None
        """
        file = None

        try:
            file = open(file_name, "w")

            json_students: list = []
            for student in student_data:
                student_json: dict = {"FirstName": student.student_first_name(),
                                      "LastName": student.student_last_name(),
                                      "CourseName": student.course_name()}
                json_students.append(student_json)

            json.dump(json_students, file, indent=2)
            file.close()

            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user.

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display.
        :param error: Exception object with technical message to display.

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Petra Chinsangaram,3.10.2026,Updated to access Student data instead of dictionary data

        :param student_data: list of dictionary rows to be displayed.

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.student_first_name()} '
                  f'{student.student_last_name()} '
                  f'is enrolled in {student.course_name()}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Petra Chinsangaram,3.10.2026,Updated to create Student object instead of dictionary

        :param student_data: list of dictionary rows to be filled with input data.

        :return: list
        """

        try:
            student = Student()

            student.student_first_name = input("Enter the student's first name: ")
            student.student_last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")

            student_data.append(student)

            print()
            print(f"You have registered {student.student_first_name()} "
                  f"{student.student_last_name()} for {student.course_name()}.")

        except ValueError as e:
            IO.output_error_messages(message=e.__str__(), error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with "
                                             "your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

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
        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                         student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
