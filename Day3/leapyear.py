year = int(input("What year you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a Leap year")