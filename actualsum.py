nums = list(map(int, input("Enter array elements: ").split()))

n = len(nums)

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)