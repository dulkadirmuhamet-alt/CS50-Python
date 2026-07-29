name = input("camelCase: ")

print("snakecase: ", end="")

# Loop through each character to find the uppercase letters
for char in name:
    if char.isupper():
        # If it's capital, print an underscore and the lowercase version
        print("_" + char.lower(), end="")
    else:
        # Otherwise, just print the character as it is
        print(char, end="")

# Print a final newline
print()

