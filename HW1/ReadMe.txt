HW1

1. (Requires Ch 1 – 3) Write a program called C2F.py that converts Celsius to Fahrenheit. The
program should ask the user for the temperature in Celsius and then display the temperature in
Fahrenheit.
1. The formula to covert Celsius to Fahrenheit is F=95
C+32
2. Display inputted values to 2 decimal points.
1. Even though you only display the value to 2 decimal points use the full number entered
for the calculations
3. Display your answer to 2 decimal points.
>>>
Please enter the temperature in Celsius: 33.5
33.50 Celsius is 92.30 Fahrenheit.
>>>
Please enter the temperature in Celsius: 100
100.00 Celsius is 212.00 Fahrenheit.
2. (Requires Ch 1 – 3) Write a program called M2K.py that converts miles to kilometers. The
program should ask the user for the distance in miles and then displays the distance in meters.
1. There are 1.60934 kilometers in a mile.
2. Display inputted values to 2 decimal points.
1. Even though you only display the value to 2 decimal points use the full number entered
for the calculations
3. Display your answer to 2 decimal points.
>>>
Please enter the distance in miles: 5.6789
5.68 miles is 9.14 kilometers
>>>
Please enter the distance in miles: 10
10.00 miles is 16.09 kilometers
ECS 10 Homework 1 Fall 2014
3. (Requires Ch 1 – 3) You are working at a bank and customers come in wanting to make a
withdrawal from their accounts. They don't want to have super fat wallets (as those are
uncomfortable to sit on) and so always ask that the money they withdraw always be given in the
fewest number of bills possible. Write a program called change.py that asks the user how much
money they wish to withdraw and then outputs the bills they received.
• Customers only make withdrawal requests for whole dollar amounts (ie they never ask for
cents)
• The bill amounts you have are 100s, 50s, 20s, 10s, 5s, and 1s
>>>
Please enter the amount of money you wish to withdraw: 1737
You received:
17 hundreds.
0 fifties.
1 twenties.
1 tens.
1 fives.
2 ones.
>>>
Please enter the amount of money you wish to withdraw: 168
You received:
1 hundreds.
1 fifties.
0 twenties.
1 tens.
1 fives.
3 ones.
4. (Requires Ch 7.3)Write a program that called capital.py that asks the user for a string and then
displays the string again but with all consonants in lowercase and all vowels in uppercase.
>>>
Please enter a string: I am 12 YEARS OLD!!!
I Am 12 yEArs Old!!!
>>>
Please enter a string: Today, is a good day to die.
tOdAy, Is A gOOd dAy tO dIE.
ECS 10 Homework 1 Fall 2014
5. (Requires Ch 7.3) HTML is a programming language used to create web-pages while LaTexX is
a programming language used to generate documents. Both of these languages have special
designations for some common characters as can be seen in the following table
Character HTML LaTeX Description
“ &ldquo; `` Left quote
” &rdquo; " Right quote
' &apos; ' Apostrophe
& &amp; & Ampersand
< &lt; < Less than
> &gt; > Greater than
{ { \{ Left curly bracket
} } \} Right curly bracket
% % \% Percent sign
Wrtie a program called html2latex.py that converts an HTML string into a LaTeX string. The
program should ask the user for an HTML string and then display the LaTex equivalent.
>>>
Please enter a HTML string: She told me that,
&ldquo;he&apos;s a total hottie.&rdquo;
She told me that, ``he's a total hottie."
>>>
Please enter a HTML string: Did you know that 7 &lt; 9 &amp;
9 &gt; 8?
Did you know that 7 < 9 & 9 > 8?
