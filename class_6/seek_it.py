import os

f = open("test_file2.txt", "w+")
f.write("Testing 123")
print(f.read())
f.seek(4)
f.write("*")
f.seek(0)
print(f.read())



if os.path.exists("test_file2.txt"):
    print("The file exists.")
