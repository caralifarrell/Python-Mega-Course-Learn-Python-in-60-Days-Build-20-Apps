"""
Coding Exercise 7
Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.

Then, create a program that:

1. reads each text file and

2. prints out the content of each file in the command line.

The expected output would be like the following:
I am a.
I am b.
I am c.
"""

files = ["a.txt","b.text","c.txt"]

for filename in files:
    file = open(filename,'r')
    reading = file.read()
    print(reading)

