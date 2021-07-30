# *
# **
# ***
# ****
# *****

# Method 1
# size = 5
# for x in range(1, size + 1):
#     print("*" * x)

# Method 2
size = 5
for y in range(1, size + 1):
    for x in range(1, y + 1):
        print("*", end="")
    print()
