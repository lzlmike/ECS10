HW3


Restrictions:
1. You must have at least 1 user defined function per problem.
2. You may not use global variables.
3. You may not import any modules
1. (10 mins) For this first problem you will be implementing a Caesarian Cipher. A Caesarian
Cipher takes a string and a shift amount and then shifts all characters by that many positions.
Write a program called cipher.py that asks the user for a string and a shift amount and then
display the the ciphered string.
1. The shift amount should be between 0 and 25
1. If the shift amount is not between 0 and 25 the program should continue asking the user
to enter a shift amount until it is a number between 0 and 25.
2. Only alphabetical characters should be ciphered
3. If a character is shifted beyond the end of the alphabet it should wrap back around to the
beginning
4. You will find the functions chr and ord very helpful. Ord takes a character and returns its
decimal ASCII value. Chr takes an integer and returns the ASCII character that is
represented by that value.
1. ord('a') #97
2. ord('B') #66
3. chr(67) # C
4. chr(100) #d
5. chr(ord('b') + 1) #c
Example 1:
Please enter a string to be ciphered: abcXYZ
Please enter a shift amount between 0 and 25: 1
bcdYZA
Example 2:
Please enter a string to be ciphered: ABCxyz 123
Please enter a shift amount between 0 and 25: 3
DEFabc 123
Example 3:
Please enter a string to be ciphered: What-did+you&say?!
Please enter a shift amount between 0 and 25: 10
Grkd-nsn+iye&cki?!
Example 4:
Please enter a string to be ciphered: Hello word
Please enter a shift amount between 0 and 25: dog
Please enter a shift amount between 0 and 25: cat
Please enter a shift amount between 0 and 25: 87
Please enter a shift amount between 0 and 25: -2
Please enter a shift amount between 0 and 25: 12
Tqxxa iadp
2. (10 mins) For this problem you will find all the prime numbers between 2 and N inclusive. A
number is prime if it is only evenly divisible by itself and 1. Write a program called primes.py
that asks the user for a number and displays all the primes between 2 and the number entered.
1. The number 1 is not prime so we won't be displaying it.
2. If the user does not enter a number greater than or equal to 2 then program should continue
to ask the user for a value until it is greater than or equal to 2.
3. The prime numbers are between 2 and N, inclusive. This means that if N is prime N should
be displayed
4. Each prime should be displayed on its own line.
5. Hint it may be helpful to think about what makes a number not prime.
Example 1:
Please enter an integer >= 2: 2
2
Example 2:
Please enter an integer >= 2: 20
2357 11
13
17
19
Example 3:
Please enter an integer >= 2: bob
Please enter an integer >= 2: cat
Please enter an integer >= 2: 1
Please enter an integer >= 2: 3
23
3. (20 mins) For this problem you will implement a grading program that functions as a possible
grade book entry program. Write a program called grades.py, that meets the following criterion
1. As per the guidelines at the top of the assignment you may NOT import any modules. This
includes the statistics module.
2. The user should be displayed with a list of options from 1 to 5
1. If the user chooses 1 they should be prompted to enter a student's name and grade
1. If the student does not appear in the grade book, the student and the grade should be
added to the grade book
2. If the student is already in the grade book their grade should be changed to the value
given
2. If the user chooses 2 they should be prompted to enter a student's name.
1. That student should be removed from the grade book
2. If the student is not in the grade book then the grade book should not be modified
but also no error should be displayed.
3. If the user chooses 3 the names and grades of all students should be displayed in
alphabetical order
4. If the user chooses 4 the following statistics for the course should be displayed: Mean,
Median, and Mode
1. The median is the middle number in a list of sorted numbers
2. The mode is the value that appears most often
1. If more there are 2 or more more numbers that appear most often then you may
display any of them.
5. If the user chooses 5 the program should terminate
6. If any other option is chosen the program should tell the user that it does not recognize
the option and ask the user for another choice.
7. All inputs besides the command choice will be valid.
8. You do not have to match the exact number of spaces I have in my output when
displaying grades and course statistics but there needs to be at least 1 space.
9. Hint: Break the problem down into small functions that each tackle one part of the
problem. For example have one function for inserting a student into the grade book,
another for calculating the mean, etc.
Example
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): bob 12
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): alice 77
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): jake 90
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 3
-----Displaying Grades-----
alice : 77
bob : 12
jake : 90
-----Done Displaying Grades-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): bob 80
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 3
-----Displaying Grades-----
alice : 77
bob : 80
jake : 90
-----Done Displaying Grades-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): max 90
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 3
-----Displaying Grades-----
alice : 77
bob : 80
jake : 90
max : 90
-----Done Displaying Grades-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 4
-----Displaying Statistics-----
Mean : 84.25
Median : 90
Mode : 90
-----Done Displaying Statistics-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 1
Enter name and points (Ex. 'Bob 95'): chris 17
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 4
-----Displaying Statistics-----
Mean : 70.80
Median : 80
Mode : 90
-----Done Displaying Statistics-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 7
Unrecognized command.
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: mike
Unrecognized command.
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 2
Enter a name to be removed (Ex. Bob): alice
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 3
-----Displaying Grades-----
bob : 80
chris : 17
jake : 90
max : 90
-----Done Displaying Grades-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 4
-----Displaying Statistics-----
Mean : 69.25
Median : 90
Mode : 90
-----Done Displaying Statistics-----
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 2
Enter a name to be removed (Ex. Bob): james
1. Add/modify student grade
2. Delete student grade
3. Print student grades
4. Display the course statistics
5. Quit
Your choice: 5
