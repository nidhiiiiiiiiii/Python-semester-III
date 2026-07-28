from datetime import date

# Decorator to add a border
def add_border(function):
    def wrapper(report):
        text = function(report)
        line = "*" * 40
        return line + "\n" + text + "\n" + line

    return wrapper

# Decorator to change text to uppercase
def uppercase(function):
    def wrapper(report):
        return function(report).upper()

    return wrapper

class Report:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.report_date = date.today().strftime("%d/%m/%Y")

    # Student report template
    @classmethod
    def student_report(cls, author, student_name, marks):
        content = (
            "Student Name: " + student_name +
            "\nMarks: " + marks
        )

        return cls("Student Report", content, author)

    # Sales report template
    @classmethod
    def sales_report(cls, author, product, revenue):
        content = (
            "Product: " + product +
            "\nRevenue: $" + revenue
        )

        return cls("Sales Report", content, author)

    # Displays the report
    def __str__(self):
        return (
            self.title +
            "\nAuthor: " + self.author +
            "\nDate: " + self.report_date +
            "\n" + self.content
        )

    # Counts the characters
    def __len__(self):
        return len(str(self))

    # Combines two reports
    def __add__(self, other):
        return str(self) + "\n\n" + str(other)

    # Compares two reports
    def __eq__(self, other):
        return self.title == other.title and self.content == other.content


# Normal function used by decorators
def display_report(report):
    return str(report)

# Main program
print("1. Student Report")
print("2. Sales Report")

choice = input("Choose report type: ")
author = input("Enter author name: ")

if choice == "1":
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    report = Report.student_report(author, name, marks)

elif choice == "2":
    product = input("Enter product name: ")
    revenue = input("Enter revenue: ")

    report = Report.sales_report(author, product, revenue)

else:
    report = Report("Unknown Report", "No content", author)

# Select formatting
format_report = display_report

upper_choice = input("Use uppercase? yes/no: ")

if upper_choice.lower() == "yes":
    format_report = uppercase(format_report)

border_choice = input("Add border? yes/no: ")

if border_choice.lower() == "yes":
    format_report = add_border(format_report)

# Display final report
print("\nFinal Report")
print(format_report(report))

# Test __len__()
print("\nNumber of characters:", len(report))