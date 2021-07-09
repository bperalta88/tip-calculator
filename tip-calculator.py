print("Welcome to the tip calculator!")

total = float(input("What was the total of your bill? $"))

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_bill = int(input("How many people to split the bill? "))

tip_percentage = percentage / 100
total_tip = total * tip_percentage
total_bill = total + total_tip
bill_per_person = total_bill / split_bill
total_amount_final = round(bill_per_person, 2)
print(f"Each person should pay ${total_amount_final}")
