import random
names = input("Give me everybody's names , separated by a comma. ")
name = names.split(", ")
#print(names)
#print(name)

choose = random.randint(0,len(name))
print(f"{name[choose]} is going to pay the bill")
