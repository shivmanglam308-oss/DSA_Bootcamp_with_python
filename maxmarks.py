# Number of semesters
sem = int(input("Enter no of semester: "))

for i in range(1, sem + 1):
    subjects = int(input(f"Enter no of subjects in {i} semester: "))
    
    marks = list(map(int, input(f"Marks obtained in semester {i}: ").split()))
    
    # Check if number of marks matches number of subjects
    if len(marks) != subjects:
        print("Number of marks does not match number of subjects.")
        continue
    
    valid = True
    for m in marks:
        if m < 0 or m > 100:
            print("You have entered invalid mark.")
            valid = False
            break
    
    if valid:
        print(f"Maximum mark in {i} semester:", max(marks))