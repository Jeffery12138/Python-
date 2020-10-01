sandwich_orders = ['tuna', 'apple', 'banana', 'beef', 'pastrami', 'pastrami', 'pastrami']
print("\nThe pastrami at the deli is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())