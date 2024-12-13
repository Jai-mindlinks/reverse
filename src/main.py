# Prompt user to input a string
input_string = input("Enter a string: ")

# Check if the input string is not empty
if input_string:
    # Reverse the input string using slicing
    reversed_string = input_string[::-1]
    # Display the reversed string
    print("The reversed string is", reversed_string)
else:
    print("Please enter a valid string.")