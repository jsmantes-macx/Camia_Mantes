# Declare variables
header1 = ("STUDENT PERFORMANCE EVALUATOR")
header2 = ("STUDENT PERFORMANCE REPORT")
score1 = 0
score2 = 0
score3 = 0
student_name = 0
sum = 0
average = 0
performance_level = 0

# Build the functions
def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    student_name = input("Enter student name: ")
    score1 = int(input("Enter Assessment 1: "))
    score2 = int(input("Enter Assessment 2: "))
    score3 = int(input("Enter Assessment 3: "))
    return student_name, score1, score2, score3

def evaluate_performance():
    sum = score1 +score2 + score3
    average = sum / 3

    if average >= 90:
        performance_level = "Outstanding"
    elif average >= 85:
        performance_level = "Very Satisfactory"
    elif average >= 80:
        performance_level = "Satisfactory"
    elif average >= 75:
        performance_level = "Fairly Satisfactory"
    else:
        performance_level = "Needs Improvement"

    return performance_level

def display_report():
    print("Assessment Scores: ", score1, ",", score2, ",", score3, ",")
    print("Average Score: ", average.f)
    print("Performance Level: ", performance_level)

# Call the functions in order
display_header()
get_student_info()
display_report()











