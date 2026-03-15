def solve_equation(a, b):
    result = a**3 + 3*a*a*b + 3*a*b*b + b**3
    return result

# Accepting input
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))   # accepted as asked in question

# Calling function
ans = solve_equation(a, b)

print("Result of the equation:", ans)