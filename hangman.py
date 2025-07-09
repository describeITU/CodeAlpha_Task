import random
word_list = ["apple", "potato", "icecream", "water"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing (remove in final version)
display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ")

    # Check if letter is in word
    if guessed_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guessed_letter:
                display[i] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")



    if '_' not in display:
        game_over = True
        print("You win.")