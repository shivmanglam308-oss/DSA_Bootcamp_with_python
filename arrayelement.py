# Number of elements
n = int(input())

# Input array
arr = list(map(int, input().split()))

count = {}

# Count occurrences
for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# Print result
for key in sorted(count):
    print(f"{key} occurs {count[key]} times")