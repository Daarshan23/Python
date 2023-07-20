num = int(input("Enter a three-digit number: "))

# # Get the individual digits of the number
# digit1 = num // 100
# digit2 = (num // 10) % 10
# digit3 = num % 10

# # Calculate the sum of the cubes of the digits
# sum_of_cubes = digit1**3 + digit2**3 + digit3**3

# # Check if the sum of the cubes is equal to the number
# if sum_of_cubes == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")
# x=float(input("Enter X:"))
# floor = x.__floor__()
# ceil=x.__ceil__()
# print("Floor is ",floor)
# print("Ceil is",ceil)


# def hugeTransactions(transaction):
#     return abs(transaction) >= 50000

# transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
# bigTransactions = list(filter(hugeTransactions, transactions))

# print(bigTransactions)