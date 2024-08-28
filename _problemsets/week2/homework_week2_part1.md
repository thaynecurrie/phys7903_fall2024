# _Python for Scientific Data Analysis_


#  Basic Python

## Homework - Week 2 (part 1 of 2) (due Sept 9)

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
