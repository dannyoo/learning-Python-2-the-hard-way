#Daniel Jimenez

from random import randint

def a():
    n1 = input("Enter your name: ")
    n2 = input("Enter an ANIMAL: ")
    n3 = input("Enter your MUSICAL INSTRUMENT: ")
    n4 = input("Enter your NOUN: ")
    n5 = input("Enter your ADJECTIVE: ")
    n6 = input("Enter your NOUN: ")
    print(f"""
Hey, {n1}, {n1}! 
The {n2} and the {n3}, 
The cow jumped over the {n4}; 
The {n5} dog laughed 
To see such sport, 
And the {n6} ran away with the spoon. 
~~ Lets begin the torture.
""")

def b():
    a = input("Enter a color: ")
    b = input("Enter a plural noun: ")
    c = input("Enter a noun: ")
    d = input("Enter a adjective: ")
    print(f"""
Roses are {a}, 
{b} are blue, 
{c} is {d}, 
and so are you.  
~~ Lets continue the torture.
""")

def c():
    a = input("Enter a place: ")
    b = input("Enter a verb: ")
    c = input("Enter a adjective: ")
    d = input("Enter a noun: ")
    e = input("Enter a adjective: ")
    print(f"""
When Mr. {c} visited {a}, he couldn't {b} becasuse of the {e} {d}.
~~ Welcome to the next world.
""")

def d():
    a = input("Enter a VERB ENDING IN 'ing'	: ")
    b = input("Enter a noun: ")
    c = input("Enter a PART OF THE BODY: ")
    d = input("Enter a ANIMAL: ")
    e = input("Enter a VERB ENDING IN 'ed': ")
    print(f"""
I was {a} down the hallway and some {b} grabbed my {3}, 
and I turned to him and said "so help me, if you {4} me again you will go the way of the {5}." 
And then he [Word Not Submitted] away. 
~~Katie's Kapers
""")
    
def e():
    a = input("Enter a ADJECTIVE: ")
    b = input("Enter a noun: ")
    c = input("Enter a NOUN (PLURAL): ")
    d = input("Enter a NOUN: ")
    e = input("Enter a VERB ENDING IN 'ed'	: ")
    print(f"""
There was an {a} woman who lived in a/an {b}. 
She had so many {c} she didn`t know what to do. 
She gave them some broth without any {d}]. 
She {e} them all soundly and put them to bed. 
~~ Only a loser...
""")
    
def f():
    a = input("VERB ENDING IN 'ING'", end="\n >")
    b = input("VERB ENDING IN 'ING'", end="\n >")
    c = input("VERB ENDING IN 'ED'", end="\n >")
    d = input("PLACE", end="\n >")
    e = input("VERB", end="\n >")
    f = input("VERB", end="\n >")
    print(f"""
Tommorrow is a new day full of new suprises and new adventures.
Such as {a} and {b}. Tommorrow leads you to the life you haven`t {c} yet. So why not plan to live today with the most adventurious and positive outlook. Because today is yesterday`s tommorrow and we all know that it`s good to do things differently. So let`s go to {d} and {e} with someone cool. Or you could just let it {f} right by.	
~~ What great tone...
""")

def g():
    a = input("NOUN", end="\n >")
    b = input("NOUN (PLURAL)", end="\n >")
    c = input("ADJECTIVE", end="\n >")
    d = input("VERB", end="\n >")
    e = input("NOUN (PLURAL)", end="\n >")
    f = input("COLOR", end="\n >")
    g = input("BODY PART", end="\n >")
    print(f"""
Be my {a}
---
{b} make the world go {c}
---
Pickachu says "I {d} you"
---
I love {e}, {f} does too
---
You make my {g} flutter	

~~SO LOVELY!~~
""")
    
def h():
    n1 = input("Enter your name: ")
    n2 = input("Enter an ANIMAL: ")
    n3 = input("Enter your MUSICAL INSTRUMENT: ")
    n4 = input("Enter your NOUN: ")
    n5 = input("Enter your ADJECTIVE: ")
    n6 = input("Enter your NOUN: ")
    print(f"""
Hi, {n1}! 
Your cousin reminds me of a {n2} who can actually play a {n3}, 
{n1} ran over the {n4};
The {n5} cousin laughed 
To see such whack problem, 
And the {n6} gave away with the {n3} that caused the main problem. 
~~ Lets quite the torture.
""")


def i():
    a = input("Enter a place: ")
    b = input("Enter a verb: ")
    c = input("Enter a adjective: ")
    d = input("Enter a noun: ")
    e = input("Enter a adjective: ")
    print(f"""
When Mrs. {c} kissed the floor {a}, he wanted to {b} ... but only with the {e} {d}.
~~ Wow Fam.
""")

def j():
    a = input("Enter a NOUN: ")
    b = input("Enter a plural noun: ")
    c = input("Enter a noun: ")
    d = input("Enter a place: ")
    e = input("Enter a adjective: ")
    f = input("Enter a noun: ")
    print(f"""
Be kind to your {a}-footed {b}
For a duck may be somebody`s {c},
Be kind to your {b} in {d}
Where the weather is always {e}.

You may think that this is the {f},
Well it is.	
""")

print(f"""
Hi there! 
Enter a number:
1 - Do 10 madlibs one at a time?
2 - Let us choose a random madlib.
""")
test = int(input("> "))


if test == 1:
    madlibs = [a(), b(), c(), d(), e(), f(), g(), h(), i(), j()]

if test == 2:
    madlibs = [a , b , c, d, e, f, g, h, i, j]
    madlibs[randint(0, (len(madlibs)-2))]()

## that extra credit tho...