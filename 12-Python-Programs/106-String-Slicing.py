"""
===============================================================================
File Name    : 106-String-Slicing.py
Description  : String Slicing in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
String slicing is used to extract a portion (substring) of a string by
specifying the start index and end index.

Syntax:
string_name[start : end : step]

Where:
start -> Starting index (included)
end   -> Ending index (excluded)
step  -> Number of positions to move

Examples:
text[0:4]
text[2:]
text[:5]
text[::2]
"""

# -----------------------------------------------------------------------------
# Creating a string.
# -----------------------------------------------------------------------------
text = "Python Programming"

# -----------------------------------------------------------------------------
# Displaying the original string.
# -----------------------------------------------------------------------------
print("Original String :", text)
# Output:
# Original String : Python Programming

print()

# -----------------------------------------------------------------------------
# Extracting characters from index 0 to 5.
# -----------------------------------------------------------------------------
print("text[0:6] :", text[0:6])
# Output:
# text[0:6] : Python

# -----------------------------------------------------------------------------
# Extracting characters from index 7 to the end.
# -----------------------------------------------------------------------------
print("text[7:] :", text[7:])
# Output:
# text[7:] : Programming

# -----------------------------------------------------------------------------
# Extracting characters from the beginning to index 6.
# -----------------------------------------------------------------------------
print("text[:6] :", text[:6])
# Output:
# text[:6] : Python

# -----------------------------------------------------------------------------
# Extracting the entire string.
# -----------------------------------------------------------------------------
print("text[:] :", text[:])
# Output:
# text[:] : Python Programming

print()

# -----------------------------------------------------------------------------
# Extracting every second character.
# -----------------------------------------------------------------------------
print("text[::2] :", text[::2])
# Output:
# text[::2] : Pto rgamn

# -----------------------------------------------------------------------------
# Extracting every third character.
# -----------------------------------------------------------------------------
print("text[::3] :", text[::3])
# Output:
# text[::3] : Ph oai

print()

# -----------------------------------------------------------------------------
# Reversing the string using slicing.
# -----------------------------------------------------------------------------
print("text[::-1] :", text[::-1])
# Output:
# text[::-1] : gnimmargorP nohtyP

print()

# -----------------------------------------------------------------------------
# Extracting the last six characters.
# -----------------------------------------------------------------------------
print("text[-6:] :", text[-6:])
# Output:
# text[-6:] : amming

# -----------------------------------------------------------------------------
# Extracting characters using negative indexes.
# -----------------------------------------------------------------------------
print("text[-11:-1] :", text[-11:-1])
# Output:
# text[-11:-1] : Programmin
