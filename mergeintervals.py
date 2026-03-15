def merge_intervals(intervals):
    # Sort intervals based on starting value
    intervals.sort()
    
    merged = []
    
    for interval in intervals:
        # If merged list is empty OR no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlapping intervals → merge them
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# Input
intervals = [[1,3],[2,6],[8,10],[15,18]]

# Function call
result = merge_intervals(intervals)

print(result)