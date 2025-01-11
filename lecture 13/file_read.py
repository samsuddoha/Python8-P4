f = open('input.txt')
lines = f.readlines()
sum = 0
for line in lines:
    num_list = line.split()
    for num in num_list:
        sum = sum + int(num)

print("Sum=", sum)