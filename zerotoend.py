# Input
nums = list(map(int, input("Enter array elements: ").split()))

j = 0  # position for next non-zero element

# Move non-zero elements forward
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1

# Fill remaining positions with 0
for i in range(j, len(nums)):
    nums[i] = 0

print(nums)