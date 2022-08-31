height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

result =round(weight/(height**2),2)


if result < 18.5:
    print(f"Your bmi is {result} and you are Underweight")
elif result < 25:
    print(f"Your bmi is {result} and you are Normal Weight")
elif result < 30:
    print(f"Your bmi is {result} and you are Over Weight")
elif result < 35:
    print(f"Your bmi is {result} and you are Obese")
else:
    print(f"Your bmi is {result} and you are Clinically obese")
