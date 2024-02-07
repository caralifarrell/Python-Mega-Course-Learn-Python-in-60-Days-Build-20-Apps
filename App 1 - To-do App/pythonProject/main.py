# App 1 - To-do App

# Section 2
# Day 1: Variables, Lists, and Print
'''
user_prompt = "Enter a to-do: "
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)

print(type(todo1))
'''

# Section 3
# Day 2: Methods & While-Loop
user_prompt = "Enter a to-do: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo) # append is a method
    print(todos)
