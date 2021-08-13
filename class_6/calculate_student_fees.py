from Constants.STUDENT_FEES import *
import Constants.STUDENT_FEES as FeeConstants

student_type = input("Are you an undergrad or graduate student? [U/Gg] >")

if student_type.upper() == "U":
    print("Your fees are {}".format(UGRAD_FEE))
else:
    print("Your fees are {}".format(FeeConstants.GRADUATE_FEE))



