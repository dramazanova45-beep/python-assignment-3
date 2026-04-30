import os
import csv



def check_files():
    print("Checking file...")

    if os.path.exists("students.csv"):
        print("File found: students.csv")
    else:
        print("Error: students.csv not found")
        return False

    print("Checking output folder...")

    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True



def load_data(filename):
    print("Loading data...")

    try:
        students = []

        file = open(filename, "r", encoding="utf-8")
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

        file.close()

        print("Data loaded successfully:", len(students), "students")
        return students

    except FileNotFoundError:
        print("Error: File '" + filename + "' not found. Please check the filename.")
        return []



def preview_data(students, n=5):
    print("First", n, "rows:")
    print("-----------------------------")

    for i in range(n):
        print(
            students[i]["student_id"], "|",
            students[i]["age"], "|",
            students[i]["gender"], "|",
            students[i]["country"], "| GPA:",
            students[i]["GPA"]
        )

    print("-----------------------------")



def analyse_gpa(students):
    gpas = []
    high = 0

    for row in students:
        try:
            gpa = float(row["GPA"])
            gpas.append(gpa)

            if gpa > 3.5:
                high = high + 1

        except ValueError:
            print("Wrong GPA value")
            continue

    result = {
        "total_students": len(gpas),
        "average_gpa": round(sum(gpas) / len(gpas), 2),
        "max_gpa": max(gpas),
        "min_gpa": min(gpas),
        "high_performers": high
    }

    print("GPA Analysis")
    print("-----------------------------")
    print("Total students:", result["total_students"])
    print("Average GPA:", result["average_gpa"])
    print("Highest GPA:", result["max_gpa"])
    print("Lowest GPA:", result["min_gpa"])
    print("Students GPA > 3.5:", result["high_performers"])
    print("-----------------------------")

    return result



def lambda_part(students):
    print("Lambda / Map / Filter")
    print("-----------------------------")

    high_gpa = list(filter(lambda x: float(x["GPA"]) > 3.8, students))
    print("Students with GPA > 3.8:", len(high_gpa))

    gpa_values = list(map(lambda x: float(x["GPA"]), students))
    print("GPA values first 5:", gpa_values[:5])

    hard_workers = list(filter(lambda x: float(x["study_hours_per_day"]) > 4, students))
    print("Students studying > 4 hrs:", len(hard_workers))

    print("-----------------------------")



ok = check_files()

if ok:
    students = load_data("students.csv")

    if len(students) > 0:
        preview_data(students)
        analyse_gpa(students)
        lambda_part(students)

# Task A4 test
load_data("wrong_file.csv")
