import math

def is_strong(num):
    # Calculate sum of factorials of digits
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += math.factorial(digit)
        temp //= 10
    return total == num

print("Strong numbers between 1 and 5000 are:")
for number in range(1, 5001):
    if is_strong(number):
        print(number)
