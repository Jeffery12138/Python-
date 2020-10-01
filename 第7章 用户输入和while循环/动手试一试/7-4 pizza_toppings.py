# style1
# prompt = "\nPlease enter the toppings of the pizza you want to order:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# topping = input(prompt)
# while topping != 'quit':
#     print("We will add the " + topping + " to the pizza.")
#     topping = input(prompt)

# style2
# prompt = "\nPlease enter the toppings of the pizza you want to order:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#     else:
#         print("We will add the " + topping + " to the pizza.")

# style3
prompt = "\nPlease enter the toppings of the pizza you want to order:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("We will add the " + topping + " to the pizza.")