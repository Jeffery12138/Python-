file_name = 'guest_book.txt'

while True:
    # 提示用户输入其名字
    name = input("Enter your name please(Enter 'q' if you want to quit):")
    if name == 'q':
        break
    else:
        print("Hi " + name + ", welcome to visit this site.")
        with open(file_name, 'a') as file_object:
            file_object.write(name + " visited the site.\n")