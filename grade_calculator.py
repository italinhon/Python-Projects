print(' ')
grade = int(input('What is your grade percentage? '))

last_number = grade % 10

# Core Requirements
pass_the_class =  False

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
   
# Stretch Challenge
pass_the_class = False

if last_number >= 7:
     sign = '+'
elif grade < 3:
     sign = '-'

else:
    sign = ''

print(' ')
print(f'You got {letter}{sign}')
print(' ')
if grade >= 70:
    print('Congratualations you passed on the class')
else: 
    print("Sorry, but you couldn't make it. Don't give up!")
print(' ')