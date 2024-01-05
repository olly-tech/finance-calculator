import math

# user reads information and enters option from menu given to them. input is converted to lowercase to recognise variations of correct input.
print("invest: to calculate the amount of interest you'll earn on your investment.\nrepay: to calculate the amount you'll have to repay on a home loan.")
calculator_choice = input("Please enter either 'invest' or 'repay' from the menu above to choose the right calculator: ")
calculator_choice = calculator_choice.lower()

# if/else statement to print error code if user input is not any option available, otherwise it will route to appropriate calculator, recognising correct term in input string.
error_code = "ERROR: option not recognised. Please refresh and try again."

#Repayment calculator
if("repay" in calculator_choice): #accounts for more variations of "repay" inputted by user. e.g., "repayment" "repaying house".
    print("Welcome to the Repayment Calculator")
    #user inputs values for repayment variables --> formatting values
    house_value = float(input("Enter the present value of your house: "))
    interest_rate = float(input("Enter your interest rate percentage: "))
    interest_rate = (interest_rate/100)/12
    months = float(input("How many months do you plan to repay your loan? "))
    #repayment calculation and output
    repayment =(interest_rate*house_value)/(1-(1+interest_rate)**(-months))
    print(f"You will pay £{repayment:.2f} every month until your house loan is repaid")

#Investment Calculator
elif ("invest" in calculator_choice):
    print("Welcome to the Investment Calculator")
    #simple and compound interest user inputs and calculator
    deposit = float(input("How much money are you depositing? "))
    interest_rate = float(input("Enter your interest rate percentage: "))
    investment_years = float(input("How many years do you plan on investing? "))
    simple_interest = deposit * (1 + (interest_rate/100)*investment_years)
    compound_interest = deposit * math.pow(1+(interest_rate/100), investment_years)
    investment_statement = f"The interest on your £{deposit:0.2f} deposit after {int(investment_years)} years is £"

    # user selecting simple or compound interest calculator and receiving output
    interest = input("Do you want simple or compound interest? ")
    if ("simple" in interest.lower()):
        print(f"{investment_statement}{simple_interest:.2f}")
    elif ("compound" in interest.lower()):
        print(f"{investment_statement}{compound_interest:.2f}")
    else:
        print(error_code) #fallback
else:
    print(error_code) #fallback




