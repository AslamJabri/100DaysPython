number = int(input("Enter the number "))

for num in range(0,number):
    if num % 3 ==0  and num %5 ==0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 :
        print("Fizz")
    else:
        print(num)
    