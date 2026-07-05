import csv

def create_grades_file():
    num_students = int(input("How many students do you want to enter? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Enter each student's information
        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam1 = int(input("Exam 1 Grade: "))
            exam2 = int(input("Exam 2 Grade: "))
            exam3 = int(input("Exam 3 Grade: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv has been created successfully!")

def main():
    create_grades_file()

main()

import csv

def display_grades():
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Read and print the header
        header = next(reader)

        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        # Print each student's record
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

def main():
    display_grades()

main()