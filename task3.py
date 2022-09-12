"""
Loan payment calculator
"""

# Get the details of the loan from the user: How much money do you owe, in dollars?​
money_owed = input('How much money do you owe, in dollars?')
# Convert input to float​
money_owed = float(money_owed)
# Get the annual percentage rate: what us the annual percentage rate?​
annual_percentage_rate = float(input('what is the annual percentage rate?'))
# Get the monthly payment: what will your monthly payment be, in dollars?​
monthly_payment = float(input('what will your monthly payment be, in dollars?'))
# Get  months to calculate results: how many months do you want to see the results for?​
months = int(input('how many months do you want to see the results for?'))
# Repeat the calculation for all the months the user  wants to see results for​
for month in range(months):
    # Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
    #   monthly_rate = apr/100/12
    monthly_rate = annual_percentage_rate/100/12
    # add in  interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    # Make payment
    money_owed = money_owed - monthly_payment
    # Print the results 
    print('-------------------------------------')
    print("Paid", round(monthly_payment,2), "of which", round(interest_paid,2), "was interest")
    print("Now, I owe", round(money_owed,2))


    # add control to check if money_owed - payment < 0 then print messages and break repetition
    # round the dollar amount to two decimals   
    if money_owed - monthly_payment < 0:
        print("the last payment is", round(money_owed,2))
        print("You pay off the loan in", month+1, "months")
        break