age = int(input("What is your current age? "))
life_span = int(input("What is the max age you want? "))
age_left = life_span - age
days = 365*age_left
months = 12*age_left
weeks = 52*age_left
print(f"You have {days} days , {weeks} weeks and {months} months left.")