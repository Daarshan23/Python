# list = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     list.append(num)

# print("The list of numbers:", list)


n = int(input("enter the number of element: "))
list = [int(input("enter a number: ")) for i in range(n)]
print("the list of numbers :", list)
