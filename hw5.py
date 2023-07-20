start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end+1):
    num_digits = len(str(num))
    sum_of_digits = 0

    for digit in str(num):
        sum_of_digits += int(digit) ** num_digits

    if num == sum_of_digits:
        print(num, "is an Armstrong number.")