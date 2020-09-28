responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("If yor could visit one place in the world, where would you go?")
    responses[name] = response
    repeat = input("Would you like to let another person to respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n----Polling Results----")
for name, response in responses.items():
    print(name + " would like to go to visit " + response + " someday.")
