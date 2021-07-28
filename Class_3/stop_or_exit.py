import sys

response = input("Would you like to exit?")

if response == "Y":
    sys.exit(1) # this is an unexpected exit.
else:
    print("ok we'll continue")

