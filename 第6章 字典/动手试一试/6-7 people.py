person_0 = {
    'first_name': 'li',
    'last_name': 'junwei',
    'age': 28,
    'city': 'jilin',
}
person_1 = {
    'first_name': 'he',
    'last_name': 'jianqiang',
    'age': 30,
    'city': 'shanxi',
}
person_2 = {
    'first_name': 'cai',
    'last_name': 'yuanyun',
    'age': 38,
    'city': 'shanghai',
}
people = [person_0, person_1, person_2]
for person in people:
    print("\nPerson name: " + person['first_name'].title() + " " + person['last_name'].title())
    print("Person age: " + str(person['age']))
    print("Person city: " + person['city'].title())