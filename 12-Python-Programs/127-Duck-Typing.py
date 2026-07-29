"""
===============================================================================
File Name    : 127-Duck-Typing.py
Description  : Duck Typing in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Duck Typing is a feature of Python in which the type of an object is less
important than the methods it provides.

If an object has the required method, it can be used regardless of its class.

In simple words:
"If it walks like a duck and quacks like a duck, it is treated as a duck."

Syntax:

class ClassName:

    def method(self):
        pass

def function(object):
    object.method()

Example:
Different classes provide the same method and can be used interchangeably.
"""

# -----------------------------------------------------------------------------
# Creating the first class.
# -----------------------------------------------------------------------------
class Dog:

    # -------------------------------------------------------------------------
    # Creating a common method.
    # -------------------------------------------------------------------------
    def speak(self):

        # ---------------------------------------------------------------------
        # Displaying the dog's sound.
        # ---------------------------------------------------------------------
        print("Dog says: Bark")


# -----------------------------------------------------------------------------
# Creating the second class.
# -----------------------------------------------------------------------------
class Cat:

    # -------------------------------------------------------------------------
    # Creating a common method.
    # -------------------------------------------------------------------------
    def speak(self):

        # ---------------------------------------------------------------------
        # Displaying the cat's sound.
        # ---------------------------------------------------------------------
        print("Cat says: Meow")


# -----------------------------------------------------------------------------
# Creating the third class.
# -----------------------------------------------------------------------------
class Cow:

    # -------------------------------------------------------------------------
    # Creating a common method.
    # -------------------------------------------------------------------------
    def speak(self):

        # ---------------------------------------------------------------------
        # Displaying the cow's sound.
        # ---------------------------------------------------------------------
        print("Cow says: Moo")


# -----------------------------------------------------------------------------
# Creating a function that accepts any object having the speak() method.
# -----------------------------------------------------------------------------
def make_sound(animal):

    # -------------------------------------------------------------------------
    # Calling the speak() method.
    # -------------------------------------------------------------------------
    animal.speak()


# -----------------------------------------------------------------------------
# Creating objects.
# -----------------------------------------------------------------------------
dog = Dog()
cat = Cat()
cow = Cow()

# -----------------------------------------------------------------------------
# Demonstrating Duck Typing.
# -----------------------------------------------------------------------------
make_sound(dog)
make_sound(cat)
make_sound(cow)

# Output:
# Dog says: Bark
# Cat says: Meow
# Cow says: Moo
