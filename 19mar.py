# result = {"Physics": 83, "Maths": 91, "Python": 100,
#           "Chemistry": 90, "java": 99, "SQL": 10}

# subject = input("Enter the name of the subject: ")
# marks = int(input("Enter the marks obtained: "))

# if subject not in result:
#     result[subject] = marks
#     print("Success")
# else:
#     print(f"{subject} already exists with marks {result[subject]}")
#     overwrite = input("Do you want to overwrite the marks yes/no: ")
#     if overwrite.lower() == "yes":
#         result[subject] = marks
#         print("Success")
#     else:
#         print("Aborted")

# print("Final Marks: ", result)

result = {"Physics": 83, "Maths": 91, "Python": 100,
          "Chemistry": 90, "java": 99, "SQL": 10}

subject = input("Enter the name of the subject: ")
marks = int(input("Enter the marks obtained: "))

old_marks = result.setdefault(subject, marks)
if old_marks == marks:
    print("Success")
else:
    print(f"{subject} already exists with marks {old_marks}")
    overwrite = input("Do you want to overwrite the marks yes-no: ")
    if overwrite.lower() == "yes":
        result[subject] = marks
        print("Success")
    else:
        print("Aborted")

print("Final Marks ", result)
