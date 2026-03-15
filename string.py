def move_hashes(s):
    hash_count = s.count('#')      # count number of '#'
    new_string = s.replace('#', '')  # remove all '#'
    
    result = '#' * hash_count + new_string
    return result


# Input
s = input("Enter the string: ")

# Output
print(move_hashes(s))