# Puzzl Intern Challenge

## Create a Rock, Paper, Scissors game.

You may use any tech (programming language) you please, there are no limitations on how you decide to present the game to the user. It could be a simple command line interface (CLI), or it could be graphic user interface (GUI) e.g. a Web browser or mobile app.

When we develop software in the real world we try to break down features (the things an application can do) into small pieces of work that can be done independently. Try and think of these tasks in isolation as separate problems, but read over all of them as your solution may affect how you approach the next task. Very roughly, plan how the entire flow will work, this will help you decide on which tech you need. Then look at each task in isolation and try to solve them one at a time. If you planned properly it shouldn't matter which order you do them in, but try finish one at a time and not all 3 together. This is a good habit to get into.

The game does not need to work, you just need to submit an attempt at solving each of the 3 tasks. This is a test of your problem solving skills, not your ability to write computer code. You can submit your solution however you please, it could be a working online application, a Github repository, an online notebook (e.g https://codepen.io/) or simply a text file containing your thought process. Pseudo code is also acceptable provided the logic is clear and understandable.

Submit your entry via email to [challenge@puzzl.co.za](mailto:challenge@puzzl.co.za?subject=Challenge%20Submission)

### Things you will need to understand:

Learning material is in javascript but these principles apply to all programming languages. So don't feel like you need to use javascript or even these references. There are plenty references online in a variety of languages.

#### Capturing a users input
There are many ways to capture a users input. Here are some options:
- HTML form via POST
- Command line input
- URL query parameters via GET

#### Conditional Statements
https://www.w3schools.com/js/js_if_else.asp

#### Data structures - Strings, Integers, Arrays
https://www.w3schools.com/js/js_strings.asp
https://www.w3schools.com/js/js_numbers.asp
https://www.w3schools.com/js/js_arrays.asp

#### Basic Algorithms
In order for a computer to be able to calculate the winner it needs some sort of way to identify and compare the options. The process and sequence the program follows is called the algorithm. In this case there are only 3 options so the algorithm is very simple. There are countless ways to solve this specific problem, here is one very basic example which does not consider a draw. See if you can determine the winner of the game below.

```js

// rock = 0
// paper = 1
// scissors = 2

user_input = 1
computer_input = 2

if (user_input > computer_input) {
	result = 'You win!'
} else if (user_input == 0 && computer_input == 2) {
	result = 'You win!'
} else {
	result = 'You lose!'
}

```

## Tasks

1. Create an interface that presents a user with following options and allows them to select one
	- Rock
	- Paper
	- Scissors


2. The user should be able to select an option and submit it to a game engine for processing
	- The engine should receive the users option
	- A computer player should select a random option (without knowledge of the users option).
	- The game engine should decide the winner based on the 2 players selected options.


3. Display the result to the user
	- Once the game engine has decided who wins the result must be displayed to the user by printing it to the screen.
	- The result should contain the computer players selected option.
	- The result should contain the winner.
