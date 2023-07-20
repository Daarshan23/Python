start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end+1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num, "is a perfect number")

print
