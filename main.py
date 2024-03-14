import random
import hangman_words
import hangman_art as art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already guessed this letter, Try Again!")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, its not in the List, You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
        
        #Join all the elements in the list and turn it into a String.
    
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(art.stages[lives])