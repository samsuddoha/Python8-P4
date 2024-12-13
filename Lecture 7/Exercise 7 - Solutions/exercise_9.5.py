#finding the prime numbers from a given list

numbers=[23,11,24,5,6,9]
for n in numbers:
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
    else:
        print(f" {n} is not a prime number.")

numbers = [23, 11, 24, 5, 6, 9]


