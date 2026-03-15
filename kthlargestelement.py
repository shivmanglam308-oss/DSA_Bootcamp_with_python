# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))

# Sort in descending order
nums.sort(reverse=True)

# Kth largest element
print("Kth largest element:", nums[k-1])