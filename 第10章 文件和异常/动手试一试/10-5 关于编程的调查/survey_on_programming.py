file_name = 'survey_on_programming.txt'

reason = ''
while reason != 'q':
    # 调查用户喜欢编程的原因
    print("Welcome to our survey, enter 'q' if you want to quit.")
    reason = input("Why do you love programming?")
    if reason != 'q':
        with open(file_name, 'a') as file_object:
            file_object.write(reason + "\n")
