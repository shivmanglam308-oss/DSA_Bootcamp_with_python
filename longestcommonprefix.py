def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# Input
strs = input("Enter strings separated by space: ").split()

# Output
print("Longest Common Prefix:", longestCommonPrefix(strs))