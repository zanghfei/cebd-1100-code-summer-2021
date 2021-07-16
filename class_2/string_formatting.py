# String formatting

str1 = "Red"
str2 = "Blue"
str3 = "Green"


print("First we have {2} then we have {1} and finally {0}".format(str1, str2, str3))

# We want this ->   colours = str1 + str2

colours = "{}{}".format(str1, str2)

print(colours)