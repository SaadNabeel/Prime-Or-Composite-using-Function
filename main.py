def prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return num, "is composite."
    return num, "is prime."

number = int(input("Enter a number: "))
num, result = prime(number)
print(num, result)

