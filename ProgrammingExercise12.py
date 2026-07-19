import csv
import numpy as np

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

def display_grades():
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)

        print("\nStudent Grades")
        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

def analyze_grades():
    # Load only the exam scores (columns 2, 3, and 4)
    grades = np.loadtxt(
        "grades.csv",
        delimiter=",",
        skiprows=1,
        usecols=(2, 3, 4)
    )

    print("\nFirst Few Rows of the Dataset:")
    print(grades[:5])

    print("\nStatistics for Each Exam")

    for i in range(grades.shape[1]):
        print(f"\nExam {i + 1}")
        print("Mean:", round(np.mean(grades[:, i]), 2))
        print("Median:", np.median(grades[:, i]))
        print("Standard Deviation:", round(np.std(grades[:, i]), 2))
        print("Minimum:", np.min(grades[:, i]))
        print("Maximum:", np.max(grades[:, i]))

    print("\nOverall Statistics")
    print("Mean:", round(np.mean(grades), 2))
    print("Median:", np.median(grades))
    print("Standard Deviation:", round(np.std(grades), 2))
    print("Minimum:", np.min(grades))
    print("Maximum:", np.max(grades))

    print("\nPass/Fail Results")

    for i in range(grades.shape[1]):
        passed = np.sum(grades[:, i] >= 60)
        failed = np.sum(grades[:, i] < 60)

        print(f"\nExam {i + 1}")
        print("Passed:", passed)
        print("Failed:", failed)

    total_grades = grades.size
    passed_grades = np.sum(grades >= 60)

    pass_percentage = (passed_grades / total_grades) * 100

    print("\nOverall Pass Percentage:", round(pass_percentage, 2), "%")

def main():
    create_grades_file()
    display_grades()
    analyze_grades()


main()