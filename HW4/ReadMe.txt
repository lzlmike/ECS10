1. (35 mins.) For this problem you will be implementing the game hangman. In hangman one
person chooses a secret word and and displays _ representing the position of each character. The
other person guesses letters in the word in an attempt to figure out what it is. If the character is
in the secret word the then all positions that contain that character are revealed. If the character
is not in the secret word then a body part of the hang man is drawn. The second person
continues guessing letters until either they reveal the entire secret word or until the hangman
figure is complete. If the word is completely revealed the second player wins. If the hangman is
completed the second player loses. Write a program called hangman.py that implements the
hangman game. Here is Wikipedia's article on hangman if you need more information on how
the game is played.
1. The second player has 7 guesses as there are 7 pieces to the hangman figure. The pieces are
added to the figure in the following order: rope, head, torso, left arm, right arm, left leg,
right leg.
2. At the beginning of the game the first player should be asked to enter the secret word. All
characters are legal excluding ? and white space characters (tab, space, newline). After the
user enters a word you should display 30 newlines so as to hide the secret word.
3. At the beginning of each round you should display in this order: The hanged man, the
partially guessed secret word, the characters guessed so far.
4. For the secret word, the characters that have not been guessed should be displayed as ?
5. Guesses for the characters in the secret word should be case insensitive. Store the entered
secret word in lowercase and convert all guessed characters to lower case.
6. Leading and trailing white space should be removed from the user's guess before checking it
7. The user must enter a guess. If they do not they should be told that they must enter a guess
and receive the prompt to enter the next character again. This should continue until the user
enters a new character.
8. If the user guesses a character that they have already guessed then they should be told that
they already guessed that character and be given the opportunity to guess again. This should
continue until the user enters a new character. These guesses should not be counted against
the user.
9. The user can only guess 1 character at a time. If the user enters more than 1 character they
should be told that they can only enter 1 character and be given the opportunity to guess
again. This should continue until the user enters a new character.
10. The letters that have been guessed so far should be displayed in sorted order.
11. If the user guesses the secret word they should be told that they guessed the secret word.
12. If the user does not guess the secret word they should be told that they failed to guess the
word and the word should be revealed.
13. You MUST USE FUNCTIONS for this program as it will make things much easier.
The are two examples of playing the hangman game below.
Example(The extra newlines after the secret word are not shown for space reasons):
Please enter a word to be guessed
that does not contain ? or white space: hello
?????
So far you have guessed:
Please enter your next guess: h
h????
So far you have guessed: h
Please enter your next guess: t
|
h????
So far you have guessed: h, t
Please enter your next guess: y
|
0
h????
So far you have guessed: h, t, y
Please enter your next guess: t
You already guessed the character: t
Please enter your next guess: y
You already guessed the character: y
Please enter your next guess: hi
You can only guess a single character.
Please enter your next guess: joke
You can only guess a single character.
Please enter your next guess: l
|
0
h?ll?
So far you have guessed: h, l, t, y
Please enter your next guess: u
|
0
|
h?ll?
So far you have guessed: h, l, t, u, y
Please enter your next guess: (
|
0
/|
h?ll?
So far you have guessed: (, h, l, t, u, y
Please enter your next guess: e
|
0
/|
hell?
So far you have guessed: (, e, h, l, t, u, y
Please enter your next guess: o
You correctly guessed the secret word: hello
Example (The extra newlines after the secret word are not shown for space reasons):
Please enter a word to be guessed
that does not contain ? or white space: don't ? me
Please enter a word to be guessed
that does not contain ? or white space: me and you
Please enter a word to be guessed
that does not contain ? or white space: ?the-system
Please enter a word to be guessed
that does not contain ? or white space: back--dash
??????????
So far you have guessed:
Please enter your next guess: joke
You can only guess a single character.
Please enter your next guess:
You must enter a guess.
Please enter your next guess: b
b?????????
So far you have guessed: b
Please enter your next guess: b
You already guessed the character: b
Please enter your next guess: a
ba?????a??
So far you have guessed: a, b
Please enter your next guess: a
You already guessed the character: a
Please enter your next guess: b
You already guessed the character: b
Please enter your next guess: bathroom
You can only guess a single character.
Please enter your next guess: 1
|
ba?????a??
So far you have guessed: 1, a, b
Please enter your next guess: /
|
0
ba?????a??
So far you have guessed: /, 1, a, b
Please enter your next guess: -
|
0
ba??--?a??
So far you have guessed: -, /, 1, a, b
Please enter your next guess: r
|
0
|
ba??--?a??
So far you have guessed: -, /, 1, a, b, r
Please enter your next guess: a
You already guessed the character: a
Please enter your next guess: q
|
0
/|
ba??--?a??
So far you have guessed: -, /, 1, a, b, q, r
Please enter your next guess: 9
|
0
/|\
ba??--?a??
So far you have guessed: -, /, 1, 9, a, b, q, r
Please enter your next guess: ^
|
0
/|\
/
ba??--?a??
So far you have guessed: -, /, 1, 9, ^, a, b, q, r
Please enter your next guess: z
|
0
/|\
/ \
You failed to guess the secret word: back—dash
1. (26 mins) For this problem you will be implementing the turn based battle system found in
Pokemon and many other games. In a battle the monsters take turns attacking each other until
one of them runs out of hit points (hp). If you have never seen a battle before you can watch one
here (don't bother watching beyond 3:35). Write a program called pokemon.py that implements
a basic 1 v 1 Pokemon battle that meets the following specifications
1. Modules Allowed
1. random
1. You will find the following functions from random vital to complete your
assignment: random.seed, random.random, and random.randint.
2. Since we are working with random here, it is absolutely VITAL that you follow the
instructions in how to call the random functions because if you don't, even if your
logic is correct, your answers won't match mine.
2. You should ask the user to enter the names for both monsters followed by the seed.
1. The names for the monsters can be anything
2. The seed must be an integer
1. Use the integer value of the seed input to initialize the random number generator via
a call to random.seed. This should be done exactly once in your program and before
any other calls to the functions in the random module are made.
2. In a normal program we wouldn't ask the user for a seed but here we are so that we
can test your programs
3. After seeding the random number generator, use random.randint to randomly choose who
will be first to attack. If a 0 is chosen the first monster goes first and if a 1 is chosen the
second monster will go first
4. Both monsters will start the battle with 100 hp and the fight will continue until the hp of one
of the monsters is 0. The last monster left standing is the winner.
5. Both monsters have access to the following moves
Name Number Accuracy Min Max Crit Chance Effect
Tackle 1 90.00% 10 20 5.00% Damage Opponent from min - max
High Jump Kick 2 75.00% 25 30 5.00% Damage Opponent from min - max
Desperate Blow 3 10.00% 50 60 5.00% Damage Opponent from min - max
Slack Off 4 95.00% 15 20 5.00% Heal Self from min - max
6. During each turn the player will choose a move
1. After a valid move is selected we will check to see if that move hit the opponent based
on that moves accuracy
1. Use random.random to check for a hit
2. If the move hits
1. We will randomly pick an integer between min and max for the strength of this
attack
1. Use random.randint to determine the strength
2. After determining strength we will then check if a crit occurred.
1. If a crit does occur the strength of the attack is doubled
1. For example if we used tackle and its strength was 19 this time and a crit
occurred its strength would then be 38.
2. Use random.random to determine if a critical hit occurred
3. If the attack was between 1 – 3 then the strength of the move is dealt to the other
monster as damage
4. If the attack was 4 then the strength of the move heals the current monster that
much.
3. If the move misses
1. If the attack was 1 – 3 then the other monster dodged the attack
2. If the attack was 4 then the monster failed to heal itself
2. No attack may deal more than the defender's current hp and no heal may heal the current
monster over 100 hp
1. To implement this we will still do the normal damage calculations in 6.1 but after the
strength of the move is determined we will reduce it if it would violate the rules in
6.2
1. For example let's say the defender has 10 hp left but the attack would deal 20
after completing 6.1., we would reduce the strength down to 10.
2. As another example let's say we are at 95 hp and we decide to heal. After
completing 6.1 we find that we would heal for 40. If we did this would put us
over 100 hp so we instead heal for 5.
2. If we are at full health and decide to heal, we still carry out all the steps in 6.1 but
the heal is counted as a failure because it would heal 0 hp.
7. After a monster makes it move the other monster is allowed to take its turn. Turns switch
until the hp of one monster reaches 0.
8. NO INPUT is guaranteed to be valid. If the user enters invalid input your program should
continue to ask them for input until valid input is entered.
2. Some Example Games on the following pages
Enter the name for your monster: Ash
Enter the name for your monster: Gary
Enter a seed value: 5
Ash has 100 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 4
Gary failed to heal itself.
Ash has 100 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 4
Ash failed to heal itself.
Ash has 100 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 1
Gary hit Ash with a Tackle dealing 13 points of damage.
Ash has 87 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 1
Gary dodged the attack.
Ash has 87 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 4
Gary failed to heal itself.
Ash has 87 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 4
Ash Slacked Off, healing 13 points of damage.
Ash has 100 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 1
Gary hit Ash with a Tackle dealing 13 points of damage.
Ash has 87 hit points remaining.
Gary has 100 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Ash hit Gary with a High Jump Kick dealing 28 points of damage.
Ash has 87 hit points remaining.
Gary has 72 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Gary hit Ash with a High Jump Kick dealing 26 points of damage.
Ash has 61 hit points remaining.
Gary has 72 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 3
Gary dodged the attack.
Ash has 61 hit points remaining.
Gary has 72 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 3
Ash dodged the attack.
Ash has 61 hit points remaining.
Gary has 72 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Ash hit Gary with a High Jump Kick dealing 25 points of damage.
Ash has 61 hit points remaining.
Gary has 47 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Gary hit Ash with a High Jump Kick dealing 26 points of damage.
Ash has 35 hit points remaining.
Gary has 47 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Ash hit Gary with a High Jump Kick dealing 26 points of damage.
Ash has 35 hit points remaining.
Gary has 21 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Gary hit Ash with a High Jump Kick dealing 26 points of damage.
Ash has 9 hit points remaining.
Gary has 21 hit points remaining.
Choose a move for Ash.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 1
Gary dodged the attack.
Ash has 9 hit points remaining.
Gary has 21 hit points remaining.
Choose a move for Gary.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 1
Gary hit Ash with a Tackle dealing 9 points of damage.
Gary won the fight.
Enter the name for your monster: Magikarp
Enter the name for your monster: Mewtwo
Enter a seed value: bad
Enter a seed value: 69hi
Enter a seed value: -3
Magikarp has 100 hit points remaining.
Mewtwo has 100 hit points remaining.
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: something
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 5
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: -2
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Magikarp hit Mewtwo with a High Jump Kick dealing 26 points of
damage.
Magikarp has 100 hit points remaining.
Mewtwo has 74 hit points remaining.
Choose a move for Mewtwo.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Mewtwo hit Magikarp with a High Jump Kick dealing 30 points of
damage.
Magikarp has 70 hit points remaining.
Mewtwo has 74 hit points remaining.
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Magikarp hit Mewtwo with a High Jump Kick dealing 28 points of
damage.
Magikarp has 70 hit points remaining.
Mewtwo has 46 hit points remaining.
Choose a move for Mewtwo.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Mewtwo hit Magikarp with a High Jump Kick dealing 30 points of
damage.
Magikarp has 40 hit points remaining.
Mewtwo has 46 hit points remaining.
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Magikarp hit Mewtwo with a High Jump Kick dealing 28 points of
damage.
Magikarp has 40 hit points remaining.
Mewtwo has 18 hit points remaining.
Choose a move for Mewtwo.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Mewtwo hit Magikarp with a High Jump Kick dealing 26 points of
damage.
Magikarp has 14 hit points remaining.
Mewtwo has 18 hit points remaining.
Choose a move for Magikarp.
1. Tackle
2. High Jump Kick
3. Desperate Blow
4. Slack Off
Enter your move: 2
Magikarp hit Mewtwo with a High Jump Kick dealing 18 points of
damage.
Magikarp won the fight.
