# It default assigns r value to open value, but need the w for writing
with open("../files/doc.txt", "r") as file:
    content = file.read()

print(content)
print(content)


