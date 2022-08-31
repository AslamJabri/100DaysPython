print('''            _                                 _    
           | |                               | |   
  ___ _   _| |__   ___ _ __ _ __  _   _ _ __ | | __
 / __| | | | '_ \ / _ \ '__| '_ \| | | | '_ \| |/ /
| (__| |_| | |_) |  __/ |  | |_) | |_| | | | |   < 
 \___|\__, |_.__/ \___|_|  | .__/ \__,_|_| |_|_|\_\
       __/ |               | |                     
      |___/                |_|                     ''')

print("Welcome to the Cyber Island")
first = input("Your Mission is to find the treasure island.Do you want to turn right or left? ")
if first == "left":
    second = input("You have reached to the shore. Do you want to swim or wait?")
    if second == "wait":
        final=input("The boat has arrived and drop you to the shore where you find 3 doors! pick a door from Red , Blue or Yellow? ")
        final = final.lower()
        if final == "blue":
            print("Eaten by Beast 👹!")
        elif final == "red":
            print("Burned by fire 🔥")
        elif final == "yellow":
            print("You Win!🫅🏻")
        else:
            print("Game Over")
    else:
        print("Attacked by Trout")
else:
    print("You are Dead!!")