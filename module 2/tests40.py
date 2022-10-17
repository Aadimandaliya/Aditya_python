# Write a Python func�on to check whether a number is in a given range

def check_range(n):
    if n in range(9,78):
        print(f"congratulations! , {n} is in the range")
    else :
        print(f"oops! , The number {n} is not in the given range.")

check_range(50)
