# Prompt user to input a string
input_string = input("Enter a string: ")

# Check if input string is empty
if input_string == "":
    print("Please enter a valid string.")
else:
    # Reverse the input string using slicing
    reversed_string = input_string[::-1]
    print("The reversed string is", reversed_string)