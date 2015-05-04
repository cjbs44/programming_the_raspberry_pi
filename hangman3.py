import random
import urllib.request

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14
guessed_letters = ''

def pick_a_word():
    randword = urllib.request.urlopen("http://randomword.setgetgo.com/get.php").read()
    frandword = randword.decode('utf-8')
    sfrandword = frandword[:-2]
    return sfrandword

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word?').lower()
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found
            display_word = display_word + '-'
    print(display_word)
    
def process_guess(guess, word):
    if len(guess) == len(word):
        return whole_word_guess(guess, word)
    elif len(guess) == 1:
        return single_letter_guess(guess,word)
    else:
        print('Your word entry does not match the length of the word, please try again!')

def single_letter_guess(guess, word):
    global lives_remaining
    global guessed_letters
    if word.find(guess) == -1:
        # word guess was incorrect
        lives_remaining = lives_remaining -1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter)  == -1:
            return False
    return True

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining = lives_remaining -1
        return False

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            print('The word was: ' + word)
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break
        

#print(pick_a_word())
play()
