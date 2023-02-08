"""
Wordle

1. Select a random word from the dictionary file
2. Let the user to input a 5-letter word
3. Color each letter accordingly:
  - Green: the letter is in the correct position
  - Yellow: the letter is not in the correct position
  - No color: the letter is not in the word
4. Give the user 5 more tries before outputting the result
"""

import random

word = ""

with open("words.txt", "r") as words_file:
    words = []
    for i, line in enumerate(words_file):
        words.append(line.strip().lower())
    words = [line for line in words if len(line) == 5]
    for i in range(random.randrange(len(words))):
        word = words[i]

tries_left = 6
while tries_left > 0:
    guess = input("Write your guess: ")

    correct = [None for _ in range(5)]
    not_correct = correct[:]
    not_found = correct[:]

    for i in range(5):
        if guess[i] in word:
            if word[i] == guess[i]:
                correct[i] = guess[i]
            else:
                not_correct[i] = guess[i]
        else:
            not_found[i] = guess[i]

    if all(correct):
        print(f"You guessed it! Congratulations!")
        break
    else:
        print("")
        print(f"Not quite yet! {tries_left} tries left.")
        print(f"Correct: {correct}")
        print(f"Not correct: {not_correct}")
        print(f"Not found: {not_found}")
        print("")

    if tries_left == 1:
        print("Sorry, better luck next time!")
        print(f"The word was '{word}'.")

    tries_left -= 1

exit(0)
