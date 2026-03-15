# Input
arr = list(map(int, input("Enter array elements: ").split()))

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate number:", num)
        break
    seen.add(num)