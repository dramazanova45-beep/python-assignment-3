import os
import csv
import json

print("Checking file...")

if os.path.exists("students.csv"):
    print("File found: students.csv")
else:
    print("Error: students.csv not found")
    exit()


print("Checking output folder...")

if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists")


students = []

file = open("students.csv", "r", encoding="utf-8")
reader = csv.DictReader(file)

for row in reader:
    students.append(row)

file.close()


print("Total students:", len(students))

print("First 5 rows:")
print("-----------------------------")

for i in range(5):
    print(
        students[i]["student_id"], "|",
        students[i]["age"], "|",
        students[i]["gender"], "|",
        students[i]["country"], "| GPA:",
        students[i]["GPA"]
    )

print("-----------------------------")


gpas = []
high = 0

for s in students:
    gpa = float(s["GPA"])
    gpas.append(gpa)

    if gpa > 3.5:
        high = high + 1

avg = sum(gpas) / len(gpas)
avg = round(avg, 2)

result = {
    "analysis": "GPA Statistics",
    "total_students": len(gpas),
    "average_gpa": avg,
    "max_gpa": max(gpas),
    "min_gpa": min(gpas),
    "high_performers": high
}

print("-----------------------------")
print("GPA Analysis")
print("-----------------------------")
print("Total students:", len(gpas))
print("Average GPA:", avg)
print("Highest GPA:", max(gpas))
print("Lowest GPA:", min(gpas))
print("Students GPA > 3.5:", high)
print("-----------------------------")


file = open("output/result.json", "w", encoding="utf-8")
json.dump(result, file, indent=4)
file.close()

print("Result saved to output/result.json")