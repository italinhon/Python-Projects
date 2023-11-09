the_list = []
item_list = None

print("\nPlease enter the items of the shopping list (type: quit to finish): ")
print()

while item_list != "quit":
    item_list = input("Item: ")

    if item_list != "quit":
        the_list.append(item_list)

print()
print("The shopping list is: ")

for item_list in the_list:
    print(item_list)

print()
print("The shopping list with indexes is: ")

for i in range(len(the_list)):
    items = the_list[i]

    print(f"{i}. {items}")

print()
change_item = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

the_list[change_item] = new_item

print()
for i in range(len(the_list)):
    item = the_list[i]
    print(f"{i}. {item}")