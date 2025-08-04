

#Prompt for the Basic Loan Information
total_loan_amount_for_the_Car = int(input("Enter the total loan amount? "))
annual_interest_rate = float(input("Enter the annual interest rate(percentage): ? "))
loan_duration = int(input("Enter the duration of your loan(years): "))

#Inquire about down payment
initial_loan_amount = total_loan_amount_for_the_Car
to_include_down_payment = bool(int(input("Enter '1' to include down payment: ")))
if to_include_down_payment:
    down_payment_amt = int(input("Enter the amount of down payment: "))
    initial_loan_amount = total_loan_amount_for_the_Car - down_payment_amt
#Calculate Monthly Payment
    if annual_interest_rate != 0:
        annual_interest_rate = annual_interest_rate / 100
    elif annual_interest_rate == 0:
        annual_interest_rate = 1
        monthly_payment_amt = initial_loan_amount / (loan_duration * 12)
#print(annual_interest_rate)