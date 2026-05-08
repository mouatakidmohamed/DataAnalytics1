# Description: This script practices using Python lists with movie titles
# Author: Mohamed Mouatakid

# Create a list of favorite movies
favorite_movies = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "Avatar",
    "Black Panther"
]

# Print a descriptive statement using len()
print("The list favorite_movies includes my top " + str(len(favorite_movies)) + " favorite movies.")

# Print the complete list
print(favorite_movies)

# Use sorted() to print the list alphabetically
print("\nUsing sorted():")
print(sorted(favorite_movies))

# Print the original list again
print(favorite_movies)

# Observation:
# sorted() prints the list in alphabetical order, but it does not permanently change the original list.

# Use .sort() to permanently sort the list
print("\nUsing .sort():")
favorite_movies.sort()
print(favorite_movies)

# Observation:
# .sort() permanently changes the original list into alphabetical order.

# Add one more movie using append()
favorite_movies.append("Spider-Man: No Way Home")

# Print updated description and updated list
print("\nAfter adding one more movie:")
print("The list favorite_movies now includes my top " + str(len(favorite_movies)) + " favorite movies.")
print(favorite_movies)

# Group comparison:
# My group members should have similar results if they used len(), sorted(), sort(), and append() correctly.
# The movie titles may be different, but the list behavior should be the same.

