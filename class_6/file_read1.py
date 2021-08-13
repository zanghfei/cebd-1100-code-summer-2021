try:
    with open('text_files\\values.txt') as file_object:
        contents = file_object.read(10)
        print(contents.rstrip())
except FileNotFoundError:
    print("The file was not found.")
except Exception:
    print("An unhandled error has occurred.")