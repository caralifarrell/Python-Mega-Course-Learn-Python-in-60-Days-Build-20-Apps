waiting_list = ["sen", "ben", "john"]
waiting_list.sort()  # Need to assign to a variable before sorting

# .sort(reverse=True) sorts non-alphabetically

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
