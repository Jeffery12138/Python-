# 7.2.2 让用户选择何时推出
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     # 推出程序时不打印quit
#     if message != 'quit':
#         print(message)

# 7.2.3 使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)