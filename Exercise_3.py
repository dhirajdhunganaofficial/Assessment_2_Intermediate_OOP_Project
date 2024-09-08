import os

#the function to read the inout file, calculate average grade scored and generate output in a file
def average_grade_scored(input_file, student_id):
    try:
        # statement to open the input file in reading mode
        with open(input_file, 'r') as file:
            grades = file.readlines()

        # Data cleaning and transformation
        total = 0
        count = 0
        for grade in grades:

            #statement to remove whitespace around an individual grade
            grade = grade.strip()

            #statement to check if the grade is a valid number or not
            if grade.isdigit():
                total += int(grade)
                count += 1
            else:
                raise ValueError(f"Invalid grade has been found: {grade}")

        if count == 0:
            raise ValueError("No valid grades are found in the file.")

        #statement to calculate the average
        average_grade = total / count

        #statement to create unique output file having the last 4 digits of student ID
        output_file = f"{student_id[-4:]}_average_grade.txt"

        #statement to  open the output file in writing mode
        with open(output_file, 'w') as file:
            file.write(f"The Average Grade achieved by student id {student_id} is: {average_grade:.2f}\n")

        print(f"\nThe Average grade has been calculated and written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file named as '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Implementation part of the program

#The input file having the grades
input_file = "grades.txt"

#student ID
student_id = "s20230452"

average_grade_scored(input_file, student_id)
