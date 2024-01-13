# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
alphabets = string.ascii_lowercase
vowels = ['a','e','i','o']


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
     
    counter = 0
    for char in secret_word:
        if char in letters_guessed:
            counter += 1 
    return len(secret_word) == counter
        
        
        
     

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    righ_letters_guessed = ''
     
    for char in secret_word:
        if char in letters_guessed:
            righ_letters_guessed += char
        else:
            righ_letters_guessed += '_ '

    return righ_letters_guessed

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
     
    remaining_word= list(alphabets)
    for letter in remaining_word:
        if letter in letters_guessed :
            remaining_word.remove(letter)
    return "".join(remaining_word)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
     
    
    letters_guessed = []
    guesses = 6
    warnings = 3
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    available_letters = get_available_letters(letters_guessed)
    is_word_guessed_yet = is_word_guessed(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word) ,"letters long.")
    print("You have", warnings, "warnings left")

    
    while not is_word_guessed_yet and guesses > 0:
        print("-------------")
        print("You have", guesses,"guesses left.")
        print("Available letters: ", available_letters)
        guessed_letter = input("Please guess a letter: ")
        
        if not guessed_letter.isalpha():
            warnings -= 1 
            print("Oops! That is not a valid letter. You have",warnings ,"warnings left: ", guessed_word)
            if warnings <= 0:
                guesses -= 1
        else:
            
            guessed_letter = str.lower(guessed_letter)
            if guessed_letter in letters_guessed:
                print("Oops! You've already guessed that letter. You now have", warnings ," warnings :",
guessed_word)
                if warnings <= 0:
                    guesses -= 1
                    
            else: 
                letters_guessed.append(guessed_letter)
                
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                available_letters = get_available_letters(letters_guessed)
                is_word_guessed_yet = is_word_guessed(secret_word, letters_guessed)
                if guessed_letter in secret_word:
                    print("Good guess: ", guessed_word)
                else:
                    print("Oops! That letter is not in my word:", guessed_word)
                    if guessed_letter in vowels :
                        guesses -= 2
                    else:
                        guesses -= 1
    
    if is_word_guessed_yet:
        unique_letters = []
        for letter in secret_word:
            if letter not in unique_letters:
                unique_letters.append(letter)
        total_score = guesses * len(unique_letters)
        print("Congratulations, you won!")
        print("Your total score for this game is: ", total_score)
        
    else:
        print("Sorry, you ran out of guesses. The word was else.")
        
 
        
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    logical_sum = []
    my_word_without_space = ''
    for letter in my_word:
        if letter != " ":
            my_word_without_space += letter
   
    
    if len(my_word_without_space) != len(other_word):
        return False
    else:
        letters_guessed = []
        for letter in my_word_without_space:
            if letter != "_":
                letters_guessed.append(letter)
        for i in range(len(my_word_without_space)):
            if my_word_without_space[i] != '_':
                is_my_word_right = my_word_without_space[i] == other_word[i]
                logical_sum.append(is_my_word_right)
                
            else:
                if other_word[i] in letters_guessed:
                    return False
    return not (False in logical_sum)
    
 
            
        



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
     
    
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
            
    print(possible_matches)
            



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
     
    secret_word = 'apple'
    letters_guessed = []
    guesses = 6
    warnings = 3
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    available_letters = get_available_letters(letters_guessed)
    is_word_guessed_yet = is_word_guessed(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word) ,"letters long.")
    print("You have", warnings, "warnings left")

    
    while not is_word_guessed_yet and guesses > 0:
        print("-------------")
        print("You have", guesses,"guesses left.")
        print("Available letters: ", available_letters)
        guessed_letter = input("Please guess a letter: ")
        
        if not guessed_letter.isalpha() and guessed_letter != "*":
            warnings -= 1 
            print("Oops! That is not a valid letter. You have",warnings ,"warnings left: ", guessed_word)
            if warnings <= 0:
                guesses -= 1
        elif guessed_letter == '*':
            print('possible matches are')
            show_possible_matches(guessed_word)            
        else:
            
            guessed_letter = str.lower(guessed_letter)
            if guessed_letter in letters_guessed:
                print("Oops! You've already guessed that letter. You now have", warnings ," warnings :",
guessed_word)
                if warnings <= 0:
                    guesses -= 1
                    
            else: 
                letters_guessed.append(guessed_letter)
                
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                available_letters = get_available_letters(letters_guessed)
                is_word_guessed_yet = is_word_guessed(secret_word, letters_guessed)
                if guessed_letter in secret_word:
                    print("Good guess: ", guessed_word)
                else:
                    print("Oops! That letter is not in my word:", guessed_word)
                    if guessed_letter in vowels :
                        guesses -= 2
                    else:
                        guesses -= 1
    
    if is_word_guessed_yet:
        unique_letters = []
        for letter in secret_word:
            if letter not in unique_letters:
                unique_letters.append(letter)
        total_score = guesses * len(unique_letters)
        print("Congratulations, you won!")
        print("Your total score for this game is: ", total_score)
        
    else:
        print("Sorry, you ran out of guesses. The word was else.")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
    



###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
