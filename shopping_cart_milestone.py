shopping_cart = []

print("Welcome to the Shopping Cart Program!")

def add_item(item):
    shopping_cart.append(item)
    print(f"'{item}' has been added to the cart")

def view_cart():
    if not shopping_cart:
        print("The shopping cart is empty.")
        
    else:
        print("The contents of the shopping cart are: ")
        for item in shopping_cart:
            print(item)


while True:

    print()
    print("Please select one of the following: ")
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    action = int(input("Please enter an action: "))


    if action == 1:
        item = str(input('What item would you like to add? '))
        add_item(item)
        
    elif action == 2:
        for item in shopping_cart:
            print("The contents of the shopping cart are: ")
            print(item)
    else:
        if action == 5:
            print("Thank you goodbye")
            break