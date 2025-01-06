def prime_num(n):
    for j in range(2, n + 1):
        m = j
        for i in range(2, m):
            if m % i == 0:
                break
        else:
            print(m)

n = int(input("n="))
prime_num(n)








