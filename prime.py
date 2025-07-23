def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Prime numbers from 1 to 100 are:", end=" ")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")
print()
