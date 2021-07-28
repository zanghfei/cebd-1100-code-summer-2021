student_passed = True
international_student = False

if international_student == True and student_passed == True:
    print("Move to mailing list")


if international_student and student_passed:
    print("OK")


if international_student and not student_passed:
    print("not ok")
    