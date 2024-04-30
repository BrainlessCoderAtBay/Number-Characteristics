def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
print("NOTE: I HAVE NO CLUE HOW TO MAKE THIS IDENTIFY INTEGER/DECIMAL/FRACTION.")
print("Number characteristics")
x_input = int(input("Enter Number: "))
if x_input % 2 == 1:
    print("Odd")
else:
    print("Even")
if x_input > 0:
    print("This is a positive integer. ")
elif x_input < 0:
    print("This is a negative integer. ")
elif x_input == 0:
    print("This integer is zero. ")
if is_prime(x_input):
    print(x_input, "is a prime number")
else:
    print(x_input, "is not a prime number")
