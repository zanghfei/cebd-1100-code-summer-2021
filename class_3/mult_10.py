# Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

while True:

    number = input("Please enter a whole number or Q to quits:")

    if number.upper() == "Q":
        print("Exiting program.")
        break
        #exit(0)

    number = int(number)

    if number % 10 == 0:
        print("Number is a multiple of 10")
    else:
        print("Number is NOT a multiple of 10")
