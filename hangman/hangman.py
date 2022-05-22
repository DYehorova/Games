import string
import random
from hangman_words import words
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # correct letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letter that have been guessed

    lives = 7

    # getting input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'Curresnt lives left: {lives}.',
              'You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters
                     else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("correct,this letter is in the word")

            else:
                lives = lives - 1
                print("incorrect, this letter is not in the word")
        elif user_letter in used_letters:
            print("Fool, you already tried this letter")

        else:
            print("This is not a valid character")
    if lives != 0:
        print(f"Congrats! You guessed a word! It is {word}")
    else:
        print(f"Oh no! You ran out of lives and died. The word was: {word}")


hangman()
