# Input
nums1 = list(map(int, input("Enter elements of first array: ").split()))
nums2 = list(map(int, input("Enter elements of second array: ").split()))

# Find intersection
result = list(set(nums1) & set(nums2))

print("Intersection:", result)