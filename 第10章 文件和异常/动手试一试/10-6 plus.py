def plus():
    """
    提示用户输入两个数字，再将他们相加并打印结果
    对ValueError异常进行捕获
    """
    while True:
        print("\nGive me two numbers, and I'll plus them.")
        print("Enter 'q' to quit.")
        try:
            first_number = input("\nFirst number:")
            if first_number == 'q':
                break
            second_number = input("Second number:")
            if second_number == 'q':
                break
            result = int(first_number) + int(second_number)
        except ValueError:
            print("Enter two numbers please.")
        else:
            print(first_number + " plus " + second_number + " equals " + str(result) + ".")


def main():
    plus()


if __name__ == '__main__':
    main()