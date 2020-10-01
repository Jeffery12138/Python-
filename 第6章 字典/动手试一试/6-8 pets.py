dog = {
    'type': 'dog',
    'master': 'Lucy',
}
cat = {
    'type': 'cat',
    'master': 'Edward',
}
pets = [dog, cat,]
for pet in pets:
    print("\nPet type: " + pet['type'])
    print("Master: " + pet['master'])