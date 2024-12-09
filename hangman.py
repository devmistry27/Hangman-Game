import random
from words import categories
from hangman_visual import lives_visual_dict
import string

def getValidWord(category, category_words):
    word = random.choice(category_words)
    while "-" in word or " " in word:
        word = random.choice(category_words)
    categories[category].remove(word)
    return word.upper()
    
def hangman():
    category = random.choice(list(categories.keys()))
    print(f"The category is: {category}")
    
    if not categories[category]:
        print(f"No more words in the {category} category. Please restart the game!")
        return
    
    word = getValidWord(category, categories[category])
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    
    lives = 7

    while len(wordLetters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(usedLetters))
        
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(wordList))
        
        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print("")
                
            else:
                lives = lives - 1
                print("Your letter,", userLetter, "is not in the word.")
                
        elif userLetter in usedLetters:
            print("You have already used that character, please try again.")
            
        else:
            print("Invalid Character! Please try again")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)

    else:
        print("Yay! You have guessed the word,",word,"!!")
        
if __name__ == "__main__":
    hangman()