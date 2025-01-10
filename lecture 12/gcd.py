m = int(input("m="))
n = int(input("n="))

min_value = min(m, n)
gcd = 1

for i in range(min_value, 1, -1):
    if m % i == 0 and n % i == 0:
        gcd = i
        break

print("gcd=", gcd)