#raise Exception("Program can't continue.")

try:
    num1 = int(input("Give me number #1 >"))
    num2 = int(input("Give me number #2 >"))

    if num2 == 0:
        raise Exception("You can't divide by zero.")

    result_of_div = num1 / num2
    print("num1 divided by num2 is : {}".format(result_of_div))


except Exception as the_exception:
    print("Sorry, cannot continue.  Please contact support.")
    print("The exception details are: {}".format(the_exception))

else:

    print("HELLO")