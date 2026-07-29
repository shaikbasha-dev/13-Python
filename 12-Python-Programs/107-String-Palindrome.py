"""
===============================================================================
File Name    : 107-String-Palindrome.py
Description  : String Palindrome in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A palindrome is a string that reads the same from left to right and from
right to left.

Examples:
MADAM
LEVEL
MALAYALAM

Syntax:
string_name[::-1]

Example:
text = "MADAM"
"""

# -----------------------------------------------------------------------------
# Taking a string as input from the user.
# -----------------------------------------------------------------------------
text = input("Enter a String : ")

# -----------------------------------------------------------------------------
# Converting the string to uppercase for case-insensitive comparison.
# -----------------------------------------------------------------------------
text = text.upper()

# -----------------------------------------------------------------------------
# Reversing the string using slicing.
# -----------------------------------------------------------------------------
reverse_text = text[::-1]

# -----------------------------------------------------------------------------
# Displaying the entered string.
# -----------------------------------------------------------------------------
print()
print("Original String :", text)
# Output:
# Original String : MADAM

# -----------------------------------------------------------------------------
# Displaying the reversed string.
# -----------------------------------------------------------------------------
print("Reversed String :", reverse_text)
# Output:
# Reversed String : MADAM

print()

# -----------------------------------------------------------------------------
# Checking whether the string is a palindrome.
# -----------------------------------------------------------------------------
if text == reverse_text:

    # -------------------------------------------------------------------------
    # Displaying the palindrome message.
    # -------------------------------------------------------------------------
    print(text, "is a Palindrome String")
    # Output:
    # MADAM is a Palindrome String

else:

    # -------------------------------------------------------------------------
    # Displaying the non-palindrome message.
    # -------------------------------------------------------------------------
    print(text, "is Not a Palindrome String")
    # Output:
    # PYTHON is Not a Palindrome String
