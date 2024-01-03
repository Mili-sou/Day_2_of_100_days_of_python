print("Welcome to tip calculator")
bill=float(input("What was the total bill?\n$"))
tip=int(input("What percentage tip would you like to give?10,12 or 15?\n"))
people=int(input("How many people to split the bill?\n"))
tip_percentage=tip/100
total_tip=bill*tip_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/people
#the next line will store the value with number printed after 2 decimal places.
final="{:.2f}".format(bill_per_person)
print(f"Each person should pay:${final}")
