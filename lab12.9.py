# CIS 2348 Homework 4 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 12.9 Exception handling to detect input string vs. integer


if __name__ == "__main__":
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        try:
            age = int(parts[1]) + 1
        except:
            age = 0
        print('{} {}'.format(name, age))

        # Get next line
        parts = input().split()
        name = parts[0]
