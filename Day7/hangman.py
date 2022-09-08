import random
from hangman_art import logo , stages
from hangman_alph import *
lives = 6
print(logo)
chosen = random.choice(word_list)
length_words = len(chosen)
display =[]
for _ in chosen:
    display += "_"
print(display)
 
end_of_game = False
while not end_of_game:
    guess = input("Guess the letter:").lower()
    if guess in display:
        print(f"You have already guessed {guess}.")

    for position in range(length_words):
        letter = chosen[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess  not in chosen:
        print(f"You have guessed {guess} ,that's not in the word  you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!!")  
    print(stages[lives])
    

    if "_" not in display:
        end_of_game = True
        print("You Win.")
print(f"The word is {chosen}!!!!")
    