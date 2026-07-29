# Define the convert function that takes a string ('text') as input
def convert(text):
    # Replace any ":)" with"🙂"
    text = text.replace(":)","🙂")
    # Replace any ":(" with "🙁")
    text= text.replace(":(","🙁")
    # Return the modified string
    return text

# Define the main function to handle user input and printing
def main():
    # prompt to user for input
    user_input = input()
    # Pass that input into the convert function and get the result
    result= convert(user_input)
    # Print the final result
    print(result)

# Call the main function at the very bottom
main()
