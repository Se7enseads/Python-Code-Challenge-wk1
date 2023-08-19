# Challenge 3: Consonant value

# A string containing the alphabet characters, where '#' represents index 0.
ALPHABET = "#abcdefghijklmnopqrstuvwxyz"

# Define a string containing the vowel characters.
VOWELS = "aeiou"


def solve(string):
    consonant_substrings = []  # List to store individual consonant substrings.
    # Variable to hold the current substring being processed.
    current_substring = ""

    # Loop through each character in the input string and determine if there are vowels or not.
    for char in string:
        if char not in VOWELS:
            # Append consonant characters to the current substring.
            current_substring += char
        else:
            if current_substring:
                # Add non-empty substrings to the list.
                consonant_substrings.append(current_substring)
            # Reset the current substring upon encountering a vowel.
            current_substring = ""
    if current_substring:
        # Append the last substring if it's not empty.
        consonant_substrings.append(current_substring)

    current_substring = ""

    max_value = 0  # Variable to store the maximum consonant value found.

    # Loop through each consonant substring to calculate its value and find the maximum.
    for substring in consonant_substrings:
        # Calculate the value of the substring.
        value = sum(ALPHABET.index(c) for c in substring)
        if value > max_value:
            # Update the maximum value if the current value is greater.
            max_value = value

    # Return the maximum consonant value found in the input string.
    return max_value


print(solve("zoxvyp"))
