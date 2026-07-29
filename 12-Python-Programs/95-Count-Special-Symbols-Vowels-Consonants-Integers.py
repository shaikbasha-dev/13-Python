"""
===============================================================================
File Name    : 95-Count-Special-Symbols-Vowels-Consonants-Integers.py
Description  : Count Special Symbols, Vowels, Consonants, and Integers
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
This program counts the number of vowels, consonants, digits (integers),
and special symbols present in a given string.

Categories:
1. Vowels
2. Consonants
3. Integers (Digits)
4. Special Symbols

Example:
Input  : Hello@123
Output :
Vowels          : 2
Consonants      : 3
Integers        : 3
Special Symbols : 1
"""

# -----------------------------------------------------------------------------
# Taking a string as input from the user.
# -----------------------------------------------------------------------------
text = input("Enter a String : ")

# -----------------------------------------------------------------------------
# Initializing all counters with zero.
# -----------------------------------------------------------------------------
vowel_count = 0
consonant_count = 0
integer_count = 0
special_symbol_count = 0

# -----------------------------------------------------------------------------
# Defining all vowels.
# -----------------------------------------------------------------------------
vowels = "AEIOUaeiou"

# -----------------------------------------------------------------------------
# Reading each character from the string.
# -----------------------------------------------------------------------------
for character in text:

    # -------------------------------------------------------------------------
    # Checking whether the character is a vowel.
    # -------------------------------------------------------------------------
    if character in vowels:
        vowel_count = vowel_count + 1

    # -------------------------------------------------------------------------
    # Checking whether the character is a consonant.
    # -------------------------------------------------------------------------
    elif character.isalpha():
        consonant_count = consonant_count + 1

    # -------------------------------------------------------------------------
    # Checking whether the character is a digit.
    # -------------------------------------------------------------------------
    elif character.isdigit():
        integer_count = integer_count + 1

    # -------------------------------------------------------------------------
    # Checking whether the character is a special symbol.
    # -------------------------------------------------------------------------
    else:
        special_symbol_count = special_symbol_count + 1

print()

# -----------------------------------------------------------------------------
# Displaying the entered string.
# -----------------------------------------------------------------------------
print("Entered String      :", text)
# Output:
# Entered String      : Hello@123

print()

# -----------------------------------------------------------------------------
# Displaying the total number of vowels.
# -----------------------------------------------------------------------------
print("Total Vowels        :", vowel_count)
# Output:
# Total Vowels        : 2

# -----------------------------------------------------------------------------
# Displaying the total number of consonants.
# -----------------------------------------------------------------------------
print("Total Consonants    :", consonant_count)
# Output:
# Total Consonants    : 3

# -----------------------------------------------------------------------------
# Displaying the total number of integers.
# -----------------------------------------------------------------------------
print("Total Integers      :", integer_count)
# Output:
# Total Integers      : 3

# -----------------------------------------------------------------------------
# Displaying the total number of special symbols.
# -----------------------------------------------------------------------------
print("Special Symbols     :", special_symbol_count)
# Output:
# Special Symbols     : 1
