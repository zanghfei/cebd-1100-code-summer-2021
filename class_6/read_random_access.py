with open('text_files\\values2.txt') as file_object:
    # print(file_object.tell())
    # print(file_object.read(1))
    # print(file_object.tell())
    print(file_object.read(10))
    file_object.seek(100)
    print(file_object.read(1))
    print(file_object.tell())
