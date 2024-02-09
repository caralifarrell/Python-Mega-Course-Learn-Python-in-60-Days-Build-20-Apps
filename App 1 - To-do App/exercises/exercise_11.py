"""
Coding Exercise 3
We have defined the same ranking list as in the previous exercise:

This time you should create a program that:

1. Contains the above list.

2 Prompts the user to input the person's name.

3. Returns the rank that person has.
"""

ranking = ['John', 'Sen', 'Lisa']

name = input("Please input the person's name: ")

rank_number = ranking.index(name) + 1

print(rank_number)
