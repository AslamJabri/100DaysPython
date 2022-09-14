def prime_checker(number):
    for i in range(2,number):
        is_prime = True
        if number % i != 0 :
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


n = int(input("Check the number: "))

prime_checker(number=n)