HW2


Restrictions:
1. You must have at least 1 user defined function per problem.
2. You may not use global variables.
1. (Time: 5 mins) Write a program called isleapyear.py that asks the user to enter a year and then
tells them if it is a leap year or not. Please view this website to see what makes a leap year a
leap year.
◦ Example 1:
Please enter a year: 2000
2000 is a leap year.
◦ Example 2:
Please enter a year: 1990
1990 is not a leap year.
2. (Time: 13 mins) You are designing the new front end interface for the registrar to enter new
students into their data base. Write a program called enter_registrar.py that asks the user for a
student's first name, last name, and their date of enrollment. The date of enrollment will be
entered as: MonthName day, Year. Your program will then output the following fixed width
string
LLLLLLLLLLFFFFFFFFFFMM/DD/YY
1. L stands for the persons last name. If the student's last name is too long it should be
truncated down to 10 characters. If the student's last name is less than 10 characters then
'-' should be added to the end of their last name until it is 10 characters long.
2. F stands for the persons first name. If the student's first name is too long it should be
truncated down to 10 characters. If the student's first name is less than 10 characters
then '-' should be added to then end of their first name until it is 10 characters long.
3. M stands for the month
4. D stands for the day of the month
5. YY stands for the last 2 digits of the year
• Example 1
Please enter the student's first name: Matthew
Please enter the student's last name: Butner
Please enter the student's enrollment date: September 21,
2008
Storing: Butner----Matthew---09/21/08
• Example 2
Please enter the student's first name: Joe
Please enter the student's last name: Maxwellson
Please enter the student's enrollment date: October 10,
2014
Storing: MaxwellsonJoe-------10/10/14
• Example 3
Please enter the student's first name: AVeryLongFirstName
Please enter the student's last name: CanThisEvenFit
Please enter the student's enrollment date: May 7, 1991
Storing: CanThisEveAVeryLongF05/07/91
• Example 4
Please enter the student's first name: Amy
Please enter the student's last name: Wu
Please enter the student's enrollment date: April 1, 2010
Storing: Wu--------Amy-------04/01/10
3.(Time 15 mins)Write a program called plural.py that asks the user for a noun and prints
out its plural form. We will be using the following rules for making a word plural
Ends With Plural Form
ch, sh, s, x, or z Add es
vowel and y Add s
a consonant and y Y becomes ies
f or fe Becomes ves
All others Add s
Hint: I suggest having functions that check if a letter is a vowel and another to check if a
letter is a consonant.
1. Examples
1.Please enter a word: boy
The plural form of boy is boys.
2.Please enter a word: loaf
The plural form of loaf is loaves.
3.Please enter a word: moose
The plural form of moose is mooses.
4. (Time: 15 mins) Write a program called frac_add that asks the user for two
fractions and prints out the sum of the fractions. In this program, the user can
enter anything and your program should not crash.
1. Valid input is defined as follows
1. Any amount of white space followed by a number followed by any amount
of white space
2. Any amount of white space followed by an optional negative sign followed
by a number followed by any amount of white space followed by a /
followed by any amount of white space followed by a positive number.
3. If your program receives invalid input it should tell the user they entered
bad input and then stop the program.
4. You can use exit(0) to terminate your program.
2. You should NOT simplify your fractions. If however the fractions have the
same denominator you should continue use that denominator in your answer.
3. Examples
1.Please enter a fraction: 5 / 8
Pleaes enter another fraction: 4/7
5/8 + 4/7 = 67/56
2.Please enter a fraction: 3/4
Pleaes enter another fraction: 5/4
3/4 + 5/4 = 8/4
3.Please enter a fraction: 3/4
Pleaes enter another fraction: bob
bob is not a valid fraction. Ending program.
4.Please enter a fraction: steve
Pleaes enter another fraction: 5/9
steve is not a valid fraction. Ending program.
5.Please enter a fraction: -6
Pleaes enter another fraction: -4 / 36
-6/1 + -4/36 = -220/36
6.Please enter a fraction: 3 / -4
Pleaes enter another fraction: 5/-6
3 / -4 is not a valid fraction. Ending program
