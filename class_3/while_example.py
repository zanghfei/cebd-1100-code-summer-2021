# a = 1
#
# while a < 10:
#     print(a)
#     # a += 1

while True:
    # Do something here
    response = int(input("Enter a positive number"))
    if response < 1:
        print("Sorry the response should be a number greater than 0")
    else:
        break

print("you entered a positive number which is {}".format(response))


