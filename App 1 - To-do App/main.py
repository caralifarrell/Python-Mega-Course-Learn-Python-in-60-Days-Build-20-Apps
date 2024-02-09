# App 1 - To-do App

# Section 2
# Day 1: Variables, Lists, and Print
"""
user_prompt = "Enter a to-do: "
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)

print(type(todo1))
"""

# Section 3
# Day 2: Methods & While-Loop
"""
user_prompt = "Enter a to-do: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)  # append is a method
    print(todos)

# dir() to get the list of methods that help
# help() to get description
"""

# Section 4
# Day 3: Match-Case and For-Loop

"""
todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()

    match user_action:  # matches the variable
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':  # | creates options that can also be accepted to execute block
            for item in todos:  # To output each to-do per line without the []
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:  # variable does not need to be defined, can be defined on the spot
            print("Hey, you entered an unknown command")

print("Bye!")
"""

# Section 5
# Day 4: List Indexing and Tuples

todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:  # matches the variable
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':  # put yourself in the user's shoes when adding features
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")
