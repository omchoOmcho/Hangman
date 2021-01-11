import random

def game():
    wordlist = ["java","python","javascrtipt","kotlin"]
    word = random.choice(wordlist)

    word_completion = "-" * len(word)
    guessed = False
    guessed_letters =[]
    guessed_words = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    tries = 8


   

    while not guessed and tries > 0:
        print()
        print(word_completion)
        guess = input("Input a letter: ")
    
        if len(guess) != 1:
            print("You should input a single letter")
        
        elif guess in guessed_letters:
            print("You've already guessed this letter")
            print("You lost!")
           
        elif guess.isupper():
            print("Please enter a lowercase English letter")
              
        elif guess not in letters:
            print("Please enter a lowercase English letter") 
            
        elif guess not in word:
            print("That letter doesn't appear in the word")
            print("You lost!")
            tries -= 1
            guessed_letters.append(guess)
        
        else:
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
        
            if "-" not in word_completion:
                guessed = True
                print("You guessed the word {}!".format(word_completion))
                print("You survived!")
        print()

    if not guessed:
        print("You lost!")

print("H A N G M A N")
    
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
      game()
    elif menu == "exit":
        break
    
