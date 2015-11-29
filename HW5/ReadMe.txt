1. Write a program called diff.py that asks the user for two files and displays the differences
between the characters in each file.
1. Your program should ask the user for the path to two different files
2. For every character that is in the same position in each file but is different between the two
files your program should display the index of those characters (starting from 0) as well as
the value of those two characters.
3. If one file is longer than the other your program should report the index of each of the
characters as well as the fact that it could not find a matching character
4. Examples:
1. Assume ex1.txt contains the contents: “batman” and ex2.txt contains the contents
“bitman” and ex3.txt contains the contents “backmans”.
1. Enter the name of the first file: ex1.txt
Enter the name of the second file: ex2.txt
Mismatch at character 1 a != i
2. Enter the name of the first file: ex2.txt
Enter the name of the second file: ex1.txt
Mismatch at character 1 i != a
3. Enter the name of the first file: ex1.txt
Enter the name of the second file: ex3.txt
Mismatch at character 2 t != c
Mismatch at character 3 m != k
Mismatch at character 4 a != m
Mismatch at character 5 n != a
Mismatch at character 6
!= n
No matching character for character 7 (s) found in
ex3.txt.
No matching character for character 8 (
) found in ex3.txt.
4. Enter the name of the first file: ex3.txt
Enter the name of the second file: ex1.txt
Mismatch at character 2 c != t
Mismatch at character 3 k != m
Mismatch at character 4 m != a
Mismatch at character 5 a != n
Mismatch at character 6 n !=
No matching character for character 7 (s) found in
ex3.txt.
No matching character for character 8 (
) found in ex3.txt.
2. For this problem you will be creating a program called grading.py that takes a directory
containing files that record how student's performed on their assignments and from these files
determines each students grades in addition to the course statistics.
1. You can only import the os module for this problem
1. If you import any other modules you will receive a 0 on this problem
2. Your program should ask the user for the directory that contains the homework files
3. Homework files
1. The name of a homework file is arbitrary
2. Each file is stored as csv and and has the following format
1. Percent Total, Percent contribution this assignment has to the student's grade,
2. Max Points,Maximum number of points on the assignment,
3. ,,
4. Last Name,First Name,Grade
5. Student 1 Last Name, Student 1 First Name, Student 1's Grade
6. Student 2 Last Name, Student 2 First Name, Student 2's Grade
7. …
3. Percent Total across all files will sum to 100
4. The names in the homework file are stored in arbitrary order
4. Your program should output the course statistics base on each student's percentage in the
class
1. The mean
2. Median
1. We will continue to use the same median as used in homework 3
3. Mode
1. There will always be a unique mode
4. Uncorrected sample standard deviation
1. Def: √ 1N
Σi
=1
N
( xi−̄x
)2
2. N: The number of items
3. xi : The value of item I
4. ̄x
: the mean
5. After displaying the course statistics your program should display each student's percent
grade in the class as well as their letter grade
1. Grades should be displayed in alphabetical order based on last name
1. If two people have the same last name then the ordering is based on their first names
2. For computing the letter grades
1. A's >= 90%
2. B's >= 80% and < 90%
3. C's >= 70% and < 80%
4. D's >= 60% and < 70%
5. F's < 60%
6. You must use functions in this assignment. Your program must have at least the following
functions. You're free to have more than just these functions if you desire
1. mean
1. returns the mean of the given numbers
2. median
1. returns the middle value of the given numbers. We are doing a simplified version
where we always take the middle number.
3. mode
1. returns the most commonly occurring number in the given numbers
4. std_dev
1. returns the uncorrected sample standard deviation of the given numbers
5. percent2Letter
1. given a percentage grade return the letter grade associated with it
6. read_homework
1. reads in 1 homework file and returns or updates the students scores on the
assignment, the number of points that assignment is worth, and the percent
contribution that it makes to the students overall grades
7. display_statistics
1. This should display the course statistics
2. This function is partially completed for you. Please make sure to use the provided
format strings so that your output matches mine
8. display_grades
1. This should display the students grades in alphabetical order.
2. This function is partially completed for you. Please make sure to use the provided
format strings so that your output matches

Example:
◦ Tests/Test1 only contains HW1.csv
◦ HW1.csv contains the following:
Percent Total,100,
Max Points,50,
,,
Last Name,First Name,Grade
Smith,John,50
Fruit,Apple,43
Dog,Lab,25
Cat,Long,36
Smith,Will,13
Veg,Carrot,50
Please enter the name of the directory
containing the homeworks: Tests/Test1
Mean | Median | Mode | Standard Deviation
72.33 | 86.00 | 100.00 | 26.97
Last Name | First Name | Percent | Letter
Cat | Long | 72.00 | C
Dog | Lab | 50.00 | F
Fruit | Apple | 86.00 | B
Smith | John | 100.00 | A
Smith | Will | 26.00 | F
Veg | Carrot | 100.00 | A
