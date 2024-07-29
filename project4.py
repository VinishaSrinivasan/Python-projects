# HANGMAN GAME #

import random

words = ['python','vijay','tata','jessie','homelander','serenity']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 9 # Number of allowed attemps

print ("Welcomr to Hangman!!!" )

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter:").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess #reveal letter
    else:
        print("That letter doesn't appera in the word.")
        attempts -= 1

#Game conculsion

if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was : " + chosen_word)
    print("You lost!")