
try:

    student_grade = "A"

    assert student_grade != "A", "Student grade in error."

    print("mail award to student")

except AssertionError as e:

    print("Sorry an error has occurred: " + str(e))

