# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Remove duplicates and sort the array
unique = sorted(set(arr))

# Check if second smallest and second largest exist
if len(unique) < 2:
    print("Second Smallest :", -1)
    print("Second Largest :", -1)
else:
    print("Second Smallest :", unique[1])
    print("Second Largest :", unique[-2])