# CIS 2348 Homework 4 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 12.7 Fat-burning heart rate
# This program calculates an adult's fat-burning heart rate, which is 70% of 220 minus the person's age.

# Calculate fat-burning heart rate
def fat_burning_heart_rate(age):
    rate = (220 - age) * 0.7
    return rate


def get_age():
    age = input()
    age = int(age)
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    else:
        return age


if __name__ == '__main__':
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {rate:.1f} bpm')
    except Exception as e:
        print(e)
        print('Could not calculate heart rate info.\n')
