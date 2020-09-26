favorite_numbers = {
    'Susan': [23, 45, 2, 3],
    'Lily': [45, 4, 6, 9],
    'Tom': [5],
    'Edward': [8, 18, 28, 38],
    'Jerry': [4, 3, 2, 1],
}
for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + str(number))
    else:
        print("\n" + name.title() + "'s favorite number is:")
        print("\t" + str(numbers[0]))