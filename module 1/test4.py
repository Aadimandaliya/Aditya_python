# given number is even or odd number

num = int(input("Enter a number: "))

mod = num % 2

if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")