# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))

n = len(nums)

# Handle cases where k > n
k = k % n

# Rotate array
rotated = nums[-k:] + nums[:-k]

print("Rotated Array:", rotated)