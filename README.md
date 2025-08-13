# Tic-Tac-Toe Bot Project

---

## Overview

---

The **main goal** with project was to learn how to code and *structure
big projects*. I also wanted to learn about algorithms.

I followed the guide and rules outlined in [Robert Heaton's
Programing Projects for advanced beginners #3](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/)

#### Important Rules
1. No generative AI
2. No copy-paste coding
3. Can use references such as Geeks4Geeks, StackOverflow, Reddit, etc
but have to follow no copy-paste rule

#### TL;DR
I learned how to break a big project down into smaller pieces, and unit test along the way.
I learned to refactor code and write modular abstract code and the basics of algorithms. I learned to staying organized by using uv with linters(flake8, mypy, ruff),
and version control with git.

## What I Knew Going In

---

- the basics
- some tips and tricks

I had a pretty solid understanding of the basic structures and datas types of python.
I had done multiple code camps as a kid and took an intro to programming for engineers
at my university. However, not of these courses never taught me how to
actually make anything bigger than a simple script or access a csv file.

Before this, I was doing small little day projects that I
would find on YouTube, but the only thing I had really 
learned from those was try/except blocks, and other
small tricks such as walrus notation or some class basics.

## The Project Experience

---
### Struggles
- Scope
- organization
- overthinking
- debugging

I had high confidence going into this project,
but even running a simple two player Tic-Tac-Toe game proved to be more complex in scope
than I would have originally thought. 

The biggest struggle I ran into where when making the algorithms and allowing
different types of algorithms to play together.

I often found myself trying to get everything in one go before and during this project,
but this type of project doesn't really allow that approach.

### Likes
- subject
- it fun to use what I've made
- Easy for friends and family to understand

Testing the programs was fun, because everyone can play Tic-Tac-Toe. This also makes easy
to impress my friends and family with the game an algorithm

## What I Learned/Improved

---

- Breaking Things Down
- Interfaces
- Unit testing
- Custom Exceptions
- How to google
- Algorithm Basics
- Simple manual caching
- Refactoring
- Git
- Linting tools
- Documentation

The main idea of this project was to learn how break projects down into smaller bite sized chunks.
Before this project, I would often try to do a bigger project I would freeze up as I tried to code it all at once and
I would get a half-baked product full of bugs. I'm usually pretty good at this is university, as I have a strong background
in math and science, so breaking down engineering problems is navigable process for me as I can think like a mechanical engineer.
But now with this project I have sort learned how to think like a programmer. Considering data structure, processing time,
data flow, data types, abstraction, modularity in how I break down a problem.

This project introduced me to the idea of interfaced for the turn system.
It was implemented sort of like this
```python
def generic_turn_function(board, move):
    # Logic
    return new_board
```
This allowed for more modularity and 'abstraction' which made it easier to add new algorithms.
It sort of reminds of the functional programming I keep hearing about on Dev-Tok.

Continuing off the main idea of breaking things down: this project also taught me the importance of unit testing.
Before this I was still using print statements littered through my code. 
But this project gave some example unit test to use on some game engine functions and how to write them.
This and learning how to use the PyCharm debugger proved instrumental in getting the main algorithm working.

This idea of having everything in separate chunks and abstracted also lead to me using doc string and linters.
Having doc strings make my code more readable and easier for look back on work and use it later, as well as other devs.
Having linters such as mypy, ruff, and flake8, allowed me to standardize my code and functions were used across multiple files,
each having up to a few hundred lines to all be neat, organized, and easy to expand on as the scope of the project increased.

I learned the basics of actually writing and using an algorithm. Before this, I knew what an algorithm was, but not
how they actually work. I also had to figure out recursive functions and while loops. Which unit testing proved very helpful in debugging.

I was also enlightened on the importance of refactoring.
About two thirds of the way through the project, in order to switch from only having one function to take turn to using whichever
algorithm, I had to refactor almost all the code. My project tree was also pretty unorganized at this point. It took me a 
entire about an hour to recode everything, but it reduced me having to rewrite or copy and paste functions ten different times, and
saved me having to import a file into another file just to import it back.

I also learned basic git actions with this project.
The guide suggested using Git as way to show progress and I did.
I found git pretty easy to use and looking at the initial commit and now,
I feel a deep sense of accomplishment.

I also used my knowledge of try and except blocks to have custom error messages in the program for improved user experience. 
For example, I created a custom exception for when the user tried to place their letter on a square that was already taken
and displayed a custom message.

Which brings me to the last thing I learned: 
how to google. Throughout the project I found myself having an idea,
and being able to implement parts of it, but not quite having all the pieces.
I did **NOT** use generative AI or copy-paste code, so I had to learn what to search.
For example, I would search "python custom exception for try/except block," 
instead of "Show custom error for when a player breaks the rules in my game."
This proved useful in many situations, such as when I was using copy() instead of deepcopy(),
and need to know "how to copy variable values to a new variable without changing original variable."
