guests = ['Jeffery', 'Wood', 'Lily', 'Zard']
print("Hi, " + guests[0] + ". I would like to have you for dinner.")
print("Hi, " + guests[1] + ". I would like to have you for dinner.")
print("Hi, " + guests[2] + ". I would like to have you for dinner.")
print("Hi, " + guests[3] + ". I would like to have you for dinner.")

print(guests.pop(0) + " can not come for dinner.")
print("I will ask Tom.")
guests.insert(0, 'Tom')

print("Hi, " + guests[0] + ". I would like to have you for dinner.")
print("Hi, " + guests[1] + ". I would like to have you for dinner.")
print("Hi, " + guests[2] + ". I would like to have you for dinner.")
print("Hi, " + guests[3] + ". I would like to have you for dinner.")

print("I have found a bigger dinner table, I will invite three more people for dinner.")

guests.insert(0, 'Lucy')
guests.insert(3, 'Bom')
guests.append('Sunny')

print("Hi, " + guests[0] + ". I would like to have you for dinner.")
print("Hi, " + guests[1] + ". I would like to have you for dinner.")
print("Hi, " + guests[2] + ". I would like to have you for dinner.")
print("Hi, " + guests[3] + ". I would like to have you for dinner.")
print("Hi, " + guests[4] + ". I would like to have you for dinner.")
print("Hi, " + guests[5] + ". I would like to have you for dinner.")
print("Hi, " + guests[6] + ". I would like to have you for dinner.")