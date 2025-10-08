# Ask the user for a positive integer
n = int(input("Enter a positive integer: "))

sum_even = 0
i = 1

while i <= n:
    if i % 2 == 0:  # Check if the number is even
        sum_even += i
    i += 1  # Increment
print(f"The sum of even numbers between 1 and {n} is {sum_even}.")