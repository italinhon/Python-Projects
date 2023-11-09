##On Line 33 I add a feature very commum in Brazil which is the Service Tax
##Generaly this tax is opitional so the user can accept or decline
##Usaly is 5% to 10% of the in Brazil

#Ask for the user meal price of the child and adult float
print(' ')
child = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of an adult's meal? "))

#How many people?
many_child = int(input("How many children are there? "))
many_adult = int(input("How many adults are there? "))
print(' ')

#Subtotal
import math
subtotal = (many_child * child) + (many_adult * adult)
print(f'Subtotal: ${subtotal:.2f}')
print(' ')

#Ask for the tax
tax_rate = float(input("What is the sales tax rate? "))
sale_tax = (subtotal * tax_rate) / 100
print(f'Sales Tax: ${sale_tax:.2f}')
total_price = subtotal + sale_tax
print(f'Total: ${total_price:.2f}')
print(' ')

#Ask for payment amout
payment_amount = float(input("What is the payment amount? "))
print(' ')

##Ask for opitional service tax
ask_service_tax = str(input("Would like to pay the Service Tax? (Yes/No): "))
if ask_service_tax.lower() in ['Yes', 'yes', 'y']:
    #Calculate the service tax always 10%
    service_tax_rate = 10
    service_tax = (service_tax_rate / 100) * total_price
    print(f'Service Tax: ${service_tax:.2f}')
    total_plus_service = total_price + ((10 / 100) * total_price)
    print(f'Total Includinng Service Tax: ${total_plus_service:.2f}')

else:
    print(f'Total: ${total_price:.2f}')
print(' ')
##Print total
print(f'Whitout Service Tax: ${total_price}')
change = payment_amount - total_price
print(f'Change: ${change:.2f}')