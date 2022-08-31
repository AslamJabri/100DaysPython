print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

full_name= name1+name2
t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")
true = t+r+u+e

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")
love = l+o+v+e

combine = str(true)+str(love)


if int(combine) < 10 or int(combine) > 90:
    print(f"Your score is {combine} , you go together like coke and mentos.")
elif int(combine) >= 40 and int(combine) <=50:
    print(f"Your score is {combine}, you are alright together.")
else:
    print(f"Your score is {combine}") 
