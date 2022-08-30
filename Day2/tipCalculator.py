print("Welcome to the tip calculator")
bill = float(input("What was the total bill ? $"))
percentage = float(input("What percent tip would you like to give? 10 , 12 or 15 ?"))
split = int(input("How many people to split the bill?"))


bill_percent = bill * (percentage/100)
final_bill = bill + bill_percent
split_person = final_bill/split
split_person = "{:.2f}".format(split_person)
print(f"Each person should pay: ${split_person}")