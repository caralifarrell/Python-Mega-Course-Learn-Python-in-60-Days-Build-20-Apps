"""
Coding Exercise 2
Take a look at the essay.txt file tab. That file contains some text.

You should create a program that reads the essay.txt file, converts the first letter of each word to uppercase and
prints out the converted text.
"""

file = open("essay.txt")
content = file.read()
content = content.title()
print(content)
