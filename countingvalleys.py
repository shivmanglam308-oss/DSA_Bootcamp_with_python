# Input
n = int(input("Enter number of steps: "))
path = input("Enter path (U for up, D for down): ")

level = 0
valleys = 0

for step in path:
    if step == 'U':
        level += 1
        if level == 0:
            valleys += 1
    elif step == 'D':
        level -= 1

print("Number of Valleys:", valleys)