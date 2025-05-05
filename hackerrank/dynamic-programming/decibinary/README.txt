Two key points in solving this problem.

First, look at sample.txt, and recognize the following pattern. 

Given a decimal value, the number of possible decibinary values 
with a number of 'digit' can be calculated with the below formula:

count[dv][digit] = count[dv - 2 ** (digit-1)][digit-1] +
                   count[dv - 2 * 2 ** (digit-1)][digit-1] +
                   .....                                   +
                   count[dv - 9 * 2 ** (digit-1)][digit-1]

                   (when dv - n * 2 ** (digit-1) > 0 for n in [1..9])

for each decimal value, the number of possible decibinary values
with the number of digits equal or less than 'digit':

count[dv][at_digit] = count[dv][digit] + count[dv][digit-1]

A list can be built with the last item the total number of
decibinary values corresponding a decimal value.

This is the table dbCountTable.

Another list is countBefore, which is the number of decibinaries
before a decimal value.

see below for example:
% python3 decibinary.py 19

dbCountTable:
0 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
1 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
2 [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
3 [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
4 [0, 1, 3, 4, 4, 4, 4, 4, 4, 4, 4]
5 [0, 1, 3, 4, 4, 4, 4, 4, 4, 4, 4]
6 [0, 1, 4, 6, 6, 6, 6, 6, 6, 6, 6]
7 [0, 1, 4, 6, 6, 6, 6, 6, 6, 6, 6]
8 [0, 1, 5, 9, 10, 10, 10, 10, 10, 10, 10]
9 [0, 1, 5, 9, 10, 10, 10, 10, 10, 10, 10]
10 [0, 0, 5, 11, 13, 13, 13, 13, 13, 13, 13]
11 [0, 0, 5, 11, 13, 13, 13, 13, 13, 13, 13]
12 [0, 0, 5, 14, 18, 18, 18, 18, 18, 18, 18]
13 [0, 0, 5, 14, 18, 18, 18, 18, 18, 18, 18]
14 [0, 0, 5, 16, 22, 22, 22, 22, 22, 22, 22]
15 [0, 0, 5, 16, 22, 22, 22, 22, 22, 22, 22]
16 [0, 0, 5, 19, 29, 30, 30, 30, 30, 30, 30]
17 [0, 0, 5, 19, 29, 30, 30, 30, 30, 30, 30]
18 [0, 0, 5, 21, 34, 36, 36, 36, 36, 36, 36]
19 [0, 0, 5, 21, 34, 36, 36, 36, 36, 36, 36]
20 [0, 0, 4, 23, 41, 45, 45, 45, 45, 45, 45]
21 [0, 0, 4, 23, 41, 45, 45, 45, 45, 45, 45]
22 [0, 0, 3, 24, 46, 52, 52, 52, 52, 52, 52]
23 [0, 0, 3, 24, 46, 52, 52, 52, 52, 52, 52]
24 [0, 0, 2, 25, 54, 64, 64, 64, 64, 64, 64]
25 [0, 0, 2, 25, 54, 64, 64, 64, 64, 64, 64]
26 [0, 0, 1, 25, 59, 72, 72, 72, 72, 72, 72]
27 [0, 0, 1, 25, 59, 72, 72, 72, 72, 72, 72]
28 [0, 0, 0, 25, 66, 84, 84, 84, 84, 84, 84]
29 [0, 0, 0, 25, 66, 84, 84, 84, 84, 84, 84]
30 [0, 0, 0, 25, 71, 93, 93, 93, 93, 93, 93]
31 [0, 0, 0, 25, 71, 93, 93, 93, 93, 93, 93]

countBefore:
[0, 1, 2, 4, 6, 10, 14, 20, 26, 36, 46, 59, 72, 90, 108, 130, 152, 182, 212, 248, 284, 329, 374, 426, 478, 542, 606, 678, 750, 834, 918, 1011, 1104]

for example, the 5th decibinary has a decimal value of 3 and it's at item 3 of the countBefore table.
the 11th, 12th, 13th, 14th: decimal value 5, at item 5 of the countBefore table.


Second, Given the above two tables, to find the nth decibinary by its 'index':
1. search the countBefore table to find the corresponding decimal value 'dv'.
   Imagine the row is expanded into a list of decibinary values, its index
   (dv_index) can be calculated by index - countBefore[dv] 
2. locate the row in the dbCountTbl
3. find the item number by 'dv_index' in the row: this is the number of digits the decibinary will have. 
4. find the decimal value (0 to 9) at that digit, this is done by substracting 
   count[dv][digit - 1], followed by substracting count[dv - 2 ** (digit - 1)][digit-1],
   ..., count[dv - i ** (digit -1)][digit-1], until dv - i ** (digit-1) is less than 
   0 or the result of the substraction is less than 0.

   as a result, find the decimal value (the cur_digit in the code) and the dv to look back
   and the its dv_index.
   Repeat the process until dv becomes 0.

5. keep track of the decibinary value at (dv, dv_index) for efficiency.

6. The dbCountTable and countBefore are expanded when needed.



Note that decibinary-2.py contains the code that was submitted
decibinary.py contains extra stuff to calculate decibinary numbers
in brute force.
