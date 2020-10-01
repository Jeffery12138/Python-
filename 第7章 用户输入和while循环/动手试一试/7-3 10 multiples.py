number = input("Tell me a number, and I will tell you if it is 10 multiples or not: ")
number = int(number)
if number % 10 == 0:
    print("The " + str(number) + " is 10 multiples.")
else:
    print("The " + str(number) + " is not 10 multiples.")
