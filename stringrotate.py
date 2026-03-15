def is_rotation(s, goal):
    if len(s) != len(goal):
        return False
    
    # Concatenate s with itself
    temp = s + s
    
    # Check if goal is a substring
    return goal in temp


# Input
s = input("Enter string s: ")
goal = input("Enter goal string: ")

# Output
print(is_rotation(s, goal))