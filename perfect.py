# # def is_perfect_number(number):
# #     if number == 1:
# #         return False
# #     if number == 2:
# #         return True
# #     if number % 2 == 0:
# #         return False
# #     for i in range(3, int(number ** 0.5) + 1, 2):
# #         if number % i == 0:
# #             print("Not.")
# #         break
# #     return True
# #Ask two integers from user and print all the perfect numbers between those two numbers.
# num = input("n : ")
# i = input("n : ")
# def perfect_numbers(start, end):
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 print(num) 
 Ask user for a 3-digit integer & print whether it's an Armstrong number or not. A 3-digit integer is an Armstrong number if sum of cubes of all of its digits equals to the number itself.