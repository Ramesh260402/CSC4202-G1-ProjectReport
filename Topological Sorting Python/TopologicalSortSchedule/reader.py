#  Title:		Csv reader implementation
#  Purpose:     This class allows the major csv files to be read and processed into a usable format for
#                   the rest of the program.
# 
#  TC:          O(n^3)

import csv
from pathlib import Path

class Reader:
    def __init__(self):
        self.courseDict = {}
        self.valid_format = [True, '']  # Stores information about the validity of the file format

    def read(self, file_name):
        if not Path(file_name).is_file():
            self.valid_format = [False, 'Incorrect file name, please re-run the program!']  # File does not exist
            return

        with open(file_name) as file:
            reader = csv.reader(file, delimiter=',', skipinitialspace=True)  # Create CSV reader object
            line = 0  # Track the line number
            for row in reader:
                if len(row) != 5:
                    self.valid_format = [False, f'Error on line {line + 1}, incorrect number of columns!']  # Invalid number of columns
                    return

                if line != 0:
                    if ']' not in row[3] or '[' not in row[3]:
                        self.valid_format = [False, f"Error on line {line + 1}, fourth column is not a list!"]  # Fourth column is not a list
                        return

                    if ']' not in row[4] or '[' not in row[4]:
                        self.valid_format = [False, f"Error on line {line + 1}, fifth column is not a list!"]  # Fifth column is not a list
                        return

                    row[3] = row[3].strip('][').split(', ')  # Convert fourth column to a list
                    row[4] = row[4].strip('][').split(', ')  # Convert fifth column to a list
                    self.courseDict[row[0]] = row[1:]  # Store course data in the dictionary

                line += 1

        self.validate_line()  # Validate the lines in the course dictionary

    def validate_line(self):
        line = 1  # Start from line 1 (excluding the header)
        for course, attributes in self.courseDict.items():
            for alternatives in attributes[2]:
                alternatives_list = alternatives.split(' | ')  # Split alternatives by '|'
                for c in alternatives_list:
                    if "|" in c:
                        self.valid_format = [False, f'Error on line {line + 1}, incorrect alternative format: use " | "!']  # Incorrect alternative format
                        return

            for semester in attributes[3]:
                if semester == "" or not semester.isdigit() or int(semester) not in (1, 2):
                    self.valid_format = [False, f'Error on line {line + 1}, incorrect quarter format: use numbers 1 or 2!']  # Incorrect quarter format
                    return

            line += 1

    def print_info(self):
        print(f'Printing the list: {self.courseDict}')  # Print the course dictionary

    def clear_error(self):
        self.valid_format = [True, '']  # Clear any error messages

    def clear(self):
        self.clear_error()  # Clear errors
        self.courseDict.clear()  # Clear the course dictionary
