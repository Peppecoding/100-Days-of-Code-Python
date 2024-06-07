# Create the initial treasure map with empty tiles
line1 = ["⬜️", "⬜️", "⬜️"]  # Create the first row of the map
line2 = ["⬜️", "⬜️", "⬜️"]  # Create the second row of the map
line3 = ["⬜️", "⬜️", "⬜️"]  # Create the third row of the map
map = [line1, line2, line3]  # Combine the rows into a 2D list representing the map

print("Hiding your treasure! X marks the spot.")  # Display a message to the user

position = input("Where do you want to put the treasure? (e.g., a2/b3) ")  # Get the treasure's position from the user

# Extract the letter and number coordinates from the position input
letter = position[0].lower()  # Get the first character (letter) and convert it to lowercase
abc = ["a", "b", "c"]  # Create a list to map letters to numerical indices
letter_index = abc.index(letter)  # Find the index of the letter in the list
number_index = int(position[1]) - 1  # Get the second character (number) and convert it to a numerical index (0-based)

# Place the treasure (X) on the map
map[number_index][letter_index] = "X"  # Update the corresponding element in the map with the treasure

# Print the final treasure map with the hidden treasure
print(f"{line1}\n{line2}\n{line3}")  # Display the map with the treasure marked by X
