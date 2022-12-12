import random
lives = 3

#create a list of secret words
words = ['happy', 'gracious', 'javascript',
         'python', 'wealth', 'command', 
          'consult', 'fulfil', 'computer',
          'unlock', 'career', 'hope']


#use the choice function of the random module to randomly pick a word
secret_word = random.choice(words)    


#create another list to store the clues
clue = list('?????')
heart_symbol = u'\u2764'

guessed_word_correctly = False

# a function to update  the clue list

def start_game(): 
    print('welcomde to ')




start_game()

def get_player_name():
    print()

    while True:
        PlayerName = input('Please enter your name: ')

        if len(PlayerName) > 3:
            break
        print("Your name is too short! :c")

    print()
    return PlayerName



get_player_name()



def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


#ask for user input to guess the letter or the word  
def validate_word(word):
    print()
   
    while len(word) > 1: 
        player_name = input('invalid word: Please enter a word: ')
        print()
    return True




while lives > 0:
    print(clue)
    print('You have' + str(heart_symbol * lives) + 'lives remaining')
    guess = input('Guess a letter or the whole word: ')
    validate_word(guess)
    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Sorry, that letter in not in the wor. You lost a life')
        lives -= 1

#check if the player has won or lost
if guessed_word_correctly:
    print('You guessed the word! You win!' + secret_word)
else:
    print('Sorry, you lost. The word was' + secret_word)