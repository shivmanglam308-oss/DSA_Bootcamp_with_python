class FindFactor:
    def find_factors(self, num):
        # If number is 0
        if num == 0:
            print("No Factors")
            return
        
        # Ignore negative sign
        num = abs(num)

        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)

        # Print factors separated by comma
        print(",".join(map(str, factors)))


# Main part
n = int(input())

obj = FindFactor()
obj.find_factors(n)