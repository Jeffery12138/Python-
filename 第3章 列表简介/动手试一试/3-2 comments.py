names = ['Lucy', 'Bob', 'Tom', 'Jack']
messages = []
for i in range(len(names)):
    message = "Hi " + names[i] + ", Nice to meet you!"
    messages.append(message)
for i in range(4):
    print(messages[i])
