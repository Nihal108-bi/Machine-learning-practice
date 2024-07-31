def Writing(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def Appending(filename, content):
    with open(filename, "a") as file:
        file.write(content)


def Reading(filename):
    with open(filename, "r") as file:
        file.read()
        print(file.read())
