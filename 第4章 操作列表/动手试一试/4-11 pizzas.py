pizzas = ['pepperoni', 'cheese', 'margarita']
friend_pizzas = pizzas[:]
pizzas.append('mozzarella')
friend_pizzas.append('deepdish')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)