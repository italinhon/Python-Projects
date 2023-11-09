print('Please enter the follow information: ')
print(' ')

first = input('First Name: ')
last = input('Last Name: ')
email = input('Email address:  ')
phone = input('Phone Number: ')
job = input('Job Title: ')
id_number = input('ID Number: ')
hair = input('Hair: ')
month = input('Month: ')
eye = input('Eyes: ')
training = input('Training: ')

print(' ')
print('The ID Card is: ')
print('-----------------------------------------')

output_0 = f'{last.upper()}, {first.title()}'
print(output_0)
print(job.title())
print('Id: ' + id_number)
print(' ')
print(email.lower())
print(phone)
output_1 = f'Hair: {hair.title()}           Eyes: {eye.title()}'
output_2 = f'Month: {month.title()}       Training: {training.title()}'
print(output_1)
print(output_2)
print('-----------------------------------------')