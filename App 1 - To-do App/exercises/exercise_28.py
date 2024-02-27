"""
Coding Exercise 4
Extend the given code so it prints out the sum of the numbers.

The output of your code should be as below:

49.1
"""

user_entries = ['10', '19.1', '20']

user_entries = [float(user_entry) for user_entry in user_entries]
print(sum(user_entries))
