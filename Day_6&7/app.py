import random  # Import the random module to enable random selection of words

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list  # Import word_list from the hangman_words.py file

chosen_word = random.choice(word_list)  # Randomly select a word from the word_list
word_length = len(chosen_word)  # Determine the length of the chosen word

end_of_game = False  # Initialize a flag to control the end of the game
lives = 6  # Set the number of lives the player starts with

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages  # Import the game logo and hangman stages from hangman_art.py
print(logo)  # Display the logo at the start of the game

# Testing code (Optional, for debugging)
# print(f'Pssst, the solution is {chosen_word}.')  # Print the solution for debugging purposes (can be removed)

# Create blanks to represent the unguessed letters in the chosen word
display = ["_"] * word_length  # Create a list of underscores, one for each letter in the chosen word
print("".join(display))  # Join the list into a string and print it to show the initial state of the word

# Start the game loop, which continues until the game is over
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # Ask the player to guess a letter and convert it to lowercase

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")  # Inform the player if they have already guessed the letter

    # Check each letter in the chosen word
    for position in range(word_length):  # Loop through each position in the chosen word
        letter = chosen_word[position]  # Get the letter at the current position
        if letter == guess:  # Check if the guessed letter matches the current letter in the word
            display[position] = letter  # If it matches, update the display list with the guessed letter

    # Check if the guess is incorrect
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")  # Inform the player the guess was wrong
        lives -= 1  # Deduct a life from the player for an incorrect guess
        if lives == 0:  # Check if the player has run out of lives
            end_of_game = True  # End the game if no lives are left
            print("You lose.")  # Inform the player they lost

    # Join all the elements in the display list into a string and print the current state of the word
    print(f"{' '.join(display)}")  # Show the word with correctly guessed letters and underscores for remaining letters

    # Check if the player has guessed the entire word
    if "_" not in display:
        end_of_game = True  # End the game if there are no more underscores (i.e., the word is fully guessed)
        print("You win.")  # Congratulate the player for winning

    # Print the current hangman stage based on the number of lives remaining
    print(stages[lives])  # Display the hangman graphic corresponding to the remaining lives
