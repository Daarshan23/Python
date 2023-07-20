# # Write a program to create a user-defined tuple of length 10. As a user, enter at least one number multiple times. Print index number of 2nd occurance of that number.
# # Ask the user to enter 10 numbers separated by spaces
# user_input = input("Enter 10 numbers separated by spaces: ")

# num_strings = user_input.split()
# num_tuple = tuple(int(num) for num in num_strings)
# target_num = int(input("Enter a number that may occur multiple times in the tuple: "))

# second_index = None
# for i in range(len(num_tuple)):
#     if num_tuple[i] == target_num:
#         if second_index is None:
#             second_index = i
#         else:
#             second_index = i
#             break

# if second_index is None:
#     print(f"{target_num} does not occur multiple times in the tuple.")
# else:
#     print(f"The index of the second occurrence of {target_num} is {second_index}")

# Ask the user to enter 10 numbers separated by spaces
# user_input = input("Enter 10 numbers separated by spaces: ")
# num_strings = user_input.split()
# num_list = [int(num) for num in num_strings]
# num_tuple = tuple(num_list)
# target_num = int(input("Enter a number that may occur multiple times in the tuple: "))
# second_index = None
# for i in range(len(num_list)):
#     if num_list[i] == target_num:
#         if second_index is None:
#             second_index = i
#         else:
#             second_index = i
#             break

# if second_index is None:
#     print(f"{target_num} does not occur multiple times in the tuple.")
# else:
#     print(f"The index of the second occurrence of {target_num} is {second_index}")



student_data =("darshan" , 19,"male")

#create 3 variables that store name of the student ,age of the student and gender of the student student_name,student_age,student_gender in python. 
student_data = ("darshan", 19, "male")

student_name = student_data[0]
student_age = student_data[1]
student_gender = student_data[2]

print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Gender: {student_gender}")
