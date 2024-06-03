print("\nWelcome to the tip calculator.\n")

# Asking for the total bill
total_bill = float(input("What was the total bill? £"))

# Valid tip percentages
valid_tips = [10, 12, 15]

# Asking for the tip percentage and ensuring it's one of the valid options
while True:
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    if tip_percentage in valid_tips:
        break
    else:
        print("Please choose a valid tip percentage (10, 12, or 15).")

# Asking for the number of people to split the bill
number_of_people = int(input("How many people to split the bill? "))

# Calculating the total payment with tip
tip_amount = total_bill * (tip_percentage / 100)
total_payment = total_bill + tip_amount

# Calculating the amount each person should pay
amount_per_person = total_payment / number_of_people

print(f"Each person should pay: ${amount_per_person:.2f}") # to round the number with two x decimal point in our float ":.2f"


