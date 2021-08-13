# I need to read a VERY large file, 2 million rows.
# when reading, I'll sum up the values of the first column in each line.

# I need to process a 100 line file, and read the records in a random order...


# Method 1

# with open("text_files\\values.txt") as file_object:
#     for l in file_object:
#         print(l, end="")  #Best way.
#         print(l.rstrip())


# Method 2

with open("text_files\\values.txt") as file_object:
    my_file = file_object.readlines()
    print(my_file)
    for l in my_file:
        print(l, end="")  #Best way.
        # print(l.rstrip())
