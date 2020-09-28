# style1
# prompt = "\nPlease enter your age, and I will tell you how much your ticket is:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# age = input(prompt)
# while age != 'quit':
#     age = int(age)
#     if age < 3:
#         print("You movie ticket is free.")
#     elif age < 12:
#         print("Your movie ticket is $10.")
#     else:
#         print("Your movie ticket is $15.")
#
#     age = input(prompt)

# style2
prompt = "\nPlease enter your age, and I will tell you how much your ticket is:"
prompt += "\n(Enter 'quit' when you are finished.)"
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("You movie ticket is free.")
        elif age < 12:
            print("Your movie ticket is $10.")
        else:
            print("Your movie ticket is $15.")

# style3
# prompt = "\nPlease enter your age, and I will tell you how much your ticket is:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             print("You movie ticket is free.")
#         elif age < 12:
#             print("Your movie ticket is $10.")
#         else:
#             print("Your movie ticket is $15.")
