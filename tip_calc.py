# Tip Calculator
# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, 
# or bad
# Calculate the tip amount and the total amount (bill amount + 
# tip amount). The tip percentage based on the level of service is 
# based on:

# good -> 20%
# fair -> 15%
# bad -> 10%
# Example session:

# $ python tip_calc.py
# Total bill amount? 100
# Level of service? good
# Tip amount: $20.00
# Total amount: $120.00
# $ python tip_calc.py
# Total bill amount? 48
# Level of service? bad
# Tip amount: $4.80
# Total amount: $52.80
# Hints:

# Remember that you need to convert the input from the user input to
# floats instead of ints. Use the float function instead of the int 
# function.


service_good = 0.2
service_fair = 0.15
service_bad = 0.1
service_whatevs = 0.05

total_bill = float(input("Total bill amount? $"))
# print(total_bill)
level_of_service = input("Level of service? ")
if level_of_service == "good":
    service_amount= service_good
elif level_of_service == "fair":
    service_amount = service_fair
elif level_of_service == "bad":
    service_amount = service_bad
else: 
    service_amount = service_whatevs

tip_amount = total_bill * service_amount

print(f"Tip amount: ${tip_amount}")
print(f"Total amount: ${total_bill + tip_amount}")