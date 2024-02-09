"""
Coding Exercise 2
Complete the code by adding a for-loop that makes the program produce the following output:
John Smith
Sen Plakay
Dora Ngacely
"""

members = ["john smith", "sen plakay", "dora ngacely"]

for name in members:
    name = name.title()
    print(name)
    