"""
Coding Exercise 1
Create a program that:

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 2.

3. Prints out the amount in euros.
"""

rate = 2

dollars = input("Please input a dollar amount: ")

dollars = float(dollars)  # Convert input to float

euros = dollars * rate

print(euros)
