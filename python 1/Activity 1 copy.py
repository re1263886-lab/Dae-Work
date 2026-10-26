wall = []

name=input("who gets a shout out? (Type 'done' when the wall is full)")

while name != "done":
    wall.append(name)
    name = input("Who else? (Type 'done' when the wall is full)")

    print()
    print("the wall so far:")