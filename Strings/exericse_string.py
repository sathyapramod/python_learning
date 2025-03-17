# 1. Print a string that uses double quotation marks inside the string.
print("String with double quotation")

# 2. Print a string that uses an apostrophe inside the string.
print("String with apostrophe: I'm here!")

# 3. Print a string that spans multiple lines with whitespace preserved.
print("""An example of string
that spans across multiple lines
and whitespace preserved.""")

# 4. Print a string that is coded on multiple lines but gets printed on a single line.
print("String with multiline "
      "displayed on a one line")

# 5. Create a string and print its length using the len() function.
Season = "Mango Season"
print(len(Season))

# 6. Create two strings, concatenate them, and print the resulting string.
first_name = "Joe"
last_name = "Alan"

full_name = first_name + last_name
print(full_name)

# 7. Create two strings and use concatenation to add a space in between them. Then print the result.
full_name = first_name + " " + last_name
print(full_name)

# 8. Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.
String = "bazinga"
print(String[2:])

# 9. Take input from the user and display that input back
usr_input = input("Say Something...\n")
print(usr_input)

# Display the input string converted to lower-case letters
print(usr_input.lower())

# Take user input and display the number of input characters.
usr_input = input("Give string as input: \n")
print(len(usr_input))

# first_letter
usr_input = input("Tell me your password:")
usr_input = usr_input.upper()
print(usr_input[0])
