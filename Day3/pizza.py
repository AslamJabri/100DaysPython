print("Welcome to Python Pizza Deliveries!")
size = input("What size of size of pizza you want? S,M or L ")
add_pep = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

final = 0


if size == "S":
    final += 15
elif size == "M":
    final += 20
else:
    final += 25

if add_pep == "Y":
    if size == "S":
        final +=2
    else:
        final +=3
if extra_cheese =="Y":
    final += 1

print(f"Your final bill is $ {final}")
