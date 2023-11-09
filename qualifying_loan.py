print('In a rating from 1 to 10:')
print(' ')
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

# For safety sake, I always like to set the variable to a default value of False
# That way, if for some reason it doesn't get set it in our rules below it will
# not be left "undefined" and cause an error, and I don't like to set the default
# to be True, because I don't want to accidentally give someone a loan!

should_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        should_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else: # This means its a small loan
    if credit_history < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else: 
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
    
# In case you are wondering, all of the above if/elif/else statements
# could be combined into one great big huge if statement, but I've left it
# this way to better match the rules that were provided.
