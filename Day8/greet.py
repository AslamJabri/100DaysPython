def greet(): #Creating the function
    fname = input("What is your name? ")
    lname = input("What is your last name? ")
    print(f"Hello {fname} {lname}")

greet() # calling the function 

def greet1(fname,lname): #Creating the function
    print(f"Hello {fname} {lname}")
    print(f"How are you {fname} {lname}")

greet1("Aslam","Jabri")


def greet2(name = "Nowhere",location = "London"):
    print(f"Hello {name}")
    print(f"How is it there in {location}")

greet2()