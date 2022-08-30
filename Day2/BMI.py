#Creating the  BMI calculator
height = float(input("What's the height in meters? "))
weight = float(input("What's is the weight? "))
bmi = weight/(height**2)
print(int(bmi))