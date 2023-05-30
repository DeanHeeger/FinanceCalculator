import math
#Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    #Calculate simple interest
    simple_interest = principal * rate * time

    #Calculate total amount
    total_amount = principal + simple_interest

    return (simple_interest, total_amount)
    

#Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, periods):
    #Calculate compound interest
    compound_interest = principal * ((1 + rate / periods) ** (periods * time) - 1)

    #Calculate total amount
    total_amount = principal * (1 + rate / periods) ** (periods * time)

    return (compound_interest, total_amount)


#Function to perform calculations based on user input
def calculate():
    print("===========================WELCOME TO OFFICE HEROES CALC===========================")
    #Prompt user to enter the operation
    while True:
        operator = input("Enter the mathematical operation (+, -, *, /, si (Simple Interest), or ci (Compound Interest)) or press '0' to exit: ")

    #Perform the appropriate calculation based on the operation
        if operator == "+":
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            
        elif operator == "-":
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            
        elif operator == "*":
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif operator == "/":
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

        elif operator == "si":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))

            simple_interest, total_amount = calculate_simple_interest(principal, rate, time)
            print(f"Simple Interest: ${simple_interest: .2f}, Total Amount: ${total_amount: .2f}")

        elif operator == "ci":
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate (as a decimal): "))
            time = float(input("Enter the time period (in years): "))
            periods = int(input("Enter the number of compounding periods per year: "))

            compound_interest, total_amount = calculate_compound_interest(principal, rate, time, periods)
            print(f"Compound Interest: ${compound_interest: .2f}, Total Amount: ${total_amount: .2f}")

        elif operator == "0":
            print("Program ended.")
            break

        else:
            print("Invalid operator!")
    print("========================================END========================================")
        
#Call calculate function to start program
calculate()
