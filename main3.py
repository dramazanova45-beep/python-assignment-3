import os
import csv
import json



class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print("File found:", self.filename)
            return True
        else:
            print("Error:", self.filename, "not found")
            return False

    def create_output_folder(self):
        print("Checking output folder...")

        if not os.path.exists("output"):
            os.makedirs("output")
            print("Output folder created")
        else:
            print("Output folder already exists")



class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            file = open(self.filename, "r", encoding="utf-8")
            reader = csv.DictReader(file)

            for row in reader:
                self.students.append(row)

            file.close()

            print("Data loaded:", len(self.students))
            return self.students

        except FileNotFoundError:
            print("File not found")
            return []

    def preview(self):
        print("First 5 rows:")
        print("----------------")

        for i in range(5):
            s = self.students[i]
            print(
                s["student_id"], "|",
                s["age"], "|",
                s["gender"], "|",
                s["country"], "| GPA:",
                s["GPA"]
            )

        print("----------------")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high = 0

        for s in self.students:
            try:
                gpa = float(s["GPA"])
                gpas.append(gpa)

                if gpa > 3.5:
                    high = high + 1

            except:
                continue

        avg = round(sum(gpas) / len(gpas), 2)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(gpas),
            "average_gpa": avg,
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high
        }

        return self.result

    def print_results(self):
        print("====== RESULT ======")
        print("Total:", self.result["total_students"])
        print("Average:", self.result["average_gpa"])
        print("Max:", self.result["max_gpa"])
        print("Min:", self.result["min_gpa"])
        print("GPA > 3.5:", self.result["high_performers"])
        print("====================")



class ResultSaver:
    def __init__(self, result):
        self.result = result

    def save(self):
        try:
            file = open("output/result.json", "w", encoding="utf-8")
            json.dump(self.result, file, indent=4)
            file.close()

            print("Saved to output/result.json")

        except:
            print("Error saving file")




fm = FileManager("students.csv")

if not fm.check_file():
    print("Stop program")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

an = DataAnalyser(dl.students)
an.analyse()
an.print_results()

rs = ResultSaver(an.result)
rs.save()
