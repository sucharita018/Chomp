# Chomp: can you avoid the poison?

#### Video Demo:  https://youtu.be/saQi98lg94A

#### Description:
I made a combinatorial game called chomp.
It is a 2x12 version in my case.
The whole game will be played against the computer in the terminal.
Let me describe the game first.
The game takes place on a 2x12 grid.
Each square is filled with a cookie, except for the bottom left one.
The bottom left piece is poison, as shown below:

🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪
💀 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪

I will be using python coordinates in this game when we want to specify some particular square.
It is a two-player game.
In our case me vs the computer.
Each player will play in turns.
When it is a player's turn, they will choose a square, and all cookies top right of that will be consumed by that player.
For example, say player 1 chooses (1,8) then the rest of the cookies would be:

🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪

💀 🍪 🍪 🍪 🍪 🍪 🍪 🍪

The goal would be to avoid the poison piece.
Since in each turn a player would have to consume at least one cookie, someone will have to consume the poison piece.
That player will loose who would be forced to consume the poison piece.

In this project, except for the main function I used four different functions.
Let me describe them one after another.
My toss() function mimics a toss to decide which player goes first.
This functions argument is input from the user (h/t).
Then a random.choice function randomly chooses between h and t.
If the user's respose matches, the user will go first.
Else, computer will have the first move.
My next function is chocolate_change().
It has two arguments (r,c).
This function will omit all cookie pieces which are top right of the (r,c)th cookie.
Then I wrote a function called next_chocolate().
This is basically the computer's move.
This function checks which cookie pieces are left and will chooses one randomly.
Then the chocolate_change() function will be applied to make the computer's move.
The last function that I wrote is display_chocolate().
The whole purpose of this function is to display the cookies nicely, since I originally coded it as a numpy array.

Let me describe the main() function now.
It will call the toss first to decide who goes first.
Then one player will start playing using either chocolate_change() or next_chocolate() function.
The game will go on till one player looses and since the grid is finite, the game will only go on for finite number of moves.
main() counts the number of moves to decide who wins the game.

In a separate file I wrote tests for those four functions. Some of my functions used random.choice. So to mock that, I used patch from unittest.mock library.
