# _Python for Scientific Data Analysis_


#  Basic Python/Data Structures

## Homework - Week 2 (due Sept 11)

### Part 1: Basic Python
### 1. Formatted Printing 

Try executing these two lines of code at Python prompt or within a Jupyter notebook cell:

```
a,b=8.3,10
print("help, the value for a is {1:3s} and for b is {2:d}".format(str(a),b))
```

Did it run? If not, fix the second line of code so that it prints out the following:

```
help, the value for a is 8.3 and for b is 10

```

Now, write a line of code that prints out the following:

```
help, the value for a is 8 and for b is 1.000000e+01
```
 
### 2. Formatted Printing and Writing

Using the Wikipedia page here -- <https://en.wikipedia.org/wiki/List_of_nearest_bright_stars> -- create a file called ``nearestAstars.txt`` and populate it with the following two lines:

```
The nearest A star is Sirius at a distance of 2.638 parsecs
the second nearest A stars is Altair at a distance of 5.1227 parsecs

```

The numbers in these lines should not be hard-coded but created with formatted print statements using the ``{}`` modern formatting style.  Assume a conversion of 3.26 pc = 1 light-year.




### 3. Argument Passing and Running Python Code

* Using equation in lecture notes #1 for the FWHM of a point source:
```
fwhm=1.028*206265*lambda*1e-6/d_tel
```

where d_tel is the telescope diameter in meters, lambda is the wavelength in microns and FWHM is the full-width-at-half-maximum of a point source in arc-seconds ...

* Write a Python script called ``compute_fwhm.py`` executable from command line that accepts lambda and d_tel as arguments and prints out the value for the FWHM

HINTS: 

1) you can name your variables to be whatever you want provided that they do not clash with something intrinsic to Python 

2) make sure you understand clearly what 'type' each thing is in your code.

### 4. Argument Passing, Importing and Running Python Code, Part 2

* Write a revised version of the Python script from Question #3 that requires the user instead to _import_ and then execute a function (from Python prompt, i.e. the thing likely starting with "<<<" on your computer). 

 Instead of just printing the answer, it should returns the value of the FWHM, where ``d_tel`` and ``lambda`` are free parameters that you can change when you call the function.  Demonstrate running this script and returning the result as a variable (i.e. >>> result = [the executed function]
 
 
### 5. Functions, If-Then Statements

Now we are going to execute a piece of code that combines multiple elements of loops, lists, etc.  Behold the bear game, listed under ``bear.py``.   

```
import numpy as np

def gold_room():
    print("This room is full of gold.  How many gold coins do you take?")

    try:
       choice = int(input("> "))
    except:
       dead("You chose a non-integer amount of coins. \n Trying in vain to break one of the coins into pieces, you upset the bear who rips your face off.")

    if how_much < 50:
        print("Nice, you're not greedy.  You escape the bear on your way out.  You Win!")
        exit(0)
    else:
        dead("You drop coins as you flee, upsetting the bear who rips your face off")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        if bear_moved == True:
         choice = input("> [take honey,taunt bear, open door] ")
        else:
         choice = input("> [take honey,taunt bear] ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Game Over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take [right, left]?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
```

* part A [you don't need to write anything for the HW, just understand this part] - figure out how to get the game started. Look at the source code to see the order in which each function is called.  Make sure you understand the ``if-then`` structures.
* part B - add another option besides the left or right door (with appropriate print statements) .  Make the outcome dependent upon chance (hint use ``np.random.rand``).

### Part 2: Data Structures

### 6. Dictionaries

Use three defined dictionaries with the following entries -- 1. city + country abbreviation, 2. country abbreviation + skyscraper, 3. skyscraper + height.   

Assume the following building heights (i.e. this will be dictionary number 3):
 Petronas Towers - 1483 ft
 WTC - 1776 ft
 Eiffel Tower - 1083 ft
 
 Write a for-loop that prints out the country, abbreviation, city, building, and height converted to au (assume 1 foot = 2.0375e-12 au):
 
 ```
The tallest building in the city of Paris, FR is the Eiffel Tower with a height of 2.207e-09 au
The tallest building in the city of New York, USA is the WTC with a height of 3.619e-09 au
The tallest building in the city of Kuala Lumpur, MY is the Petronas Towers with a height of 3.022e-09 au
 ```

### 7. Lists, Arrays, Loops and Type Conversions:

Start with a list 4 elements long, including a mix of floating point numbers and integers: $\pi$, e, 3.1 and 5.

Remove 3.1 using the ``remove`` function and array indexing.  

Append Euler's gamma constant to the list

Write a line of code that prints out ``a``, repeated 3 times

Write a line of code that prints out each element of ``a`` multiplied by 3

Write a for-loop that prints out each element of ``a`` multiplied by 3

### 8. Slicing 

Consider the array:

``a=[2,3,5,6,8,9,10]``

Use slicing to produce the following:

 ``[2,5,8,10]``
 
 ``[6,8,9]``
 
 ``[10, 9, 8, 6, 5, 3, 2]``
 
### 9. Slicing 
 
 Convert ``a`` to an array and then use conditional/boolean slicing to print out
 
 ``array([ 6,  8,  9, 10])``
 
 
 ``array([ 2,  8,  9, 10])``

