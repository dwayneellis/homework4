# homework4

                          ************  READ ME **************


# CIS 2348 Homework 4 Fall 2020.
# Due Date: 12/02/2020
# Dwayne Ellis
# Student ID: 0833810


This file serves as a guide to describe the content of this assignment.


In homework 4 we were given 4 labs (12.7, 12.9, 14.11, & 14.13) to complete.

The labs and their descriptions are as follow:


************Lab 12.7*********************

Lab 12.7 - Fat-burning heart rate

In this lab we were instructed to write a program that will calculates an adult's fat-burning heart rate. This is calculate by computing 70% of 220 minus the person's age.

The screnario is as follow:

Write a program that calculates an adult's fat-burning heart rate, which is 70% of 220 minus the person's age. Complete fat_burning_heart_rate() to calculate the fat burning heart rate.

The adult's age must be between the ages of 18 and 75 inclusive. If the age entered is not in this range, raise a ValueError exception in get_age() with the message "Invalid age." Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."

Ex: If the input is:

35
the output is:

Fat burning heart rate for a 35 year-old: 129.5 bpm
If the input is:

17
the output is:

Invalid age.
Could not calculate heart rate info.


************END OF Lab 12.7 *************


************Lab 12.9*********************

Lab 12.9 - Exception handling to detect input string vs. integer

In this lab we were instructed to write a program that reads a list of single-word first names and ages and out the list with the age incremented. 

The scenario is as follow:

The given program reads a list of single-word first names and ages (ending with -1), and outputs that list with the age incremented. The program fails and throws an exception if the second input on a line is a string rather than an integer. At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.

Ex: If the input is:

Lee 18
Lua 21
Mary Beth 19
Stu 33
-1
then the output is:

Lee 19
Lua 22
Mary 0
Stu 34

************END OF Lab 12.9 *************


************Lab 14.11 *******************

Lab 14.11 - Descending selection sort with output during execution

In this lab we were instructed to write a program that sorts the list and output in decending order.

The scenario is as follow:

Write the function selection_sort_descend_trace() that takes an integer list and sorts the list into descending order. The function should use nested loops and output the list after each iteration of the outer loop, thus outputting the list N-1 times (where N is the size).

Complete __main__ to read in a list of integers, and then call selection_sort_descend_trace() to sort the list.

Ex: If the input is:

20 10 30 40
then the output is:

40 10 30 20 
40 30 10 20 
40 30 20 10 

************END OF Lab 14.11 *************


************Lab 14.3**********************

Lab 14.13 - Sorting user IDs

In this lab we were instructed to write a program that sort user IDs in ascending order using Quicksort algorithm.

The scenarrio is as follow:

Given code that reads user IDs (until -1), complete the quicksort() and partition() functions to sort the IDs in ascending order using the Quicksort algorithm. Increment the global variable num_calls in quicksort() to keep track of how many times quicksort() is called. The given code outputs num_calls followed by the sorted IDs.

Ex: If the input is:

kaylasimms 
julia 
myron1994 
kaylajones 
-1
the output is:

7
julia 
kaylajones
kaylasimms
myron1994 

************END OF Lab 14.13 *************


************END OF Homework 4 *************


                   ************END OF READ ME File *************

