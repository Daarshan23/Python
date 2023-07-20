# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def display_details(self):
#         print("Car Details:")
#         print(f"name: {self.name}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

#     def change_details(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#         print("Car details updated.")

#     def delete(self):
#         del self


# def main():
#     cars = []
#     while True:
#         print("\n1. Add a new car")
#         print("2. Display details of an existing car")
#         print("3. Change details of an existing car")
#         print("4. Delete a car")
#         print("5. Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             name = input("Enter the name of the car: ")
#             model = input("Enter the model of the car: ")
#             year = int(input("Enter the year of the car: "))
#             car = Car(name, model, year)
#             cars.append(car)
#             print("Car added successfully.")

#         elif choice == 2:
#             if len(cars) == 0:
#                 print("No cars available.")
#             else:
#                 index = int(input("Enter the index of the car: "))
#                 if index >= 0 and index < len(cars):
#                     cars[index].display_details()
#                 else:
#                     print("Invalid car index.")

#         elif choice == 3:
#             if len(cars) == 0:
#                 print("No cars available.")
#             else:
#                 index = int(input("Enter the index of the car: "))
#                 if index >= 0 and index < len(cars):
#                     name = input("Enter the new make of the car: ")
#                     model = input("Enter the new model of the car: ")
#                     year = int(input("Enter the new year of the car: "))
#                     cars[index].change_details(name, model, year)
#                 else:
#                     print("Invalid car index.")

#         elif choice == 4:
#             if len(cars) == 0:
#                 print("No cars available.")
#             else:
#                 index = int(input("Enter the index of the car: "))
#                 if index >= 0 and index < len(cars):
#                     cars[index].delete()
#                     del cars[index]
#                     print("Car deleted successfully.")
#                 else:
#                     print("Invalid car index.")

#         elif choice == 5:
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()

# print 
# -----------------------------------------------------------------------------------------
# 4 Pillars of OOP: Inheritance, Polymorphism, Abstraction, Encapsulation
# inheritance

# Single/single level/simple inheritance
class Father():
    vehicle = "car"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)

class Child(Father):
    pass


f1 = Father()
f1.name = "Anuj"
# print(f1.vehicle)
f1.showProperties()

c1 = Child()
c1.name = "Moksh"
# print(c1.vehicle)
c1.showProperties()


# Multi-level inheritance
class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class GrandChild(Child):
    profession = "Student"

f1 = Father()
f1.name = "Harshad"

c1 = Child()
c1.name = "Anuj"
# c1.showProperties()

gc1 = GrandChild()
gc1.name = "Moksh"

gc1.showProperties()

# MRO: Method Resolution Order
# Hierachical Inheritance

class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child1(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class Child2(Father):
    vehicle = "XUV700"

f1 = Father()
f1.name = "Harshad"

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"


# Hybrid Inheritance

class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)

class Child1(Father):
    profession = "Scrum Master"
    vehicle = "Fortuner"

class Child2(Father):
    vehicle = "XUV700"

class GrandChild1(Child1):
    profession = "Student"

class GrandChild2(Child2):
    profession = "Data Scientist"

f1 = Father()
f1.name = "Harshad"

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"


# Multiple Inheritance

class Father():
    vehicle = "Honda City"
    profession = "Lawyer"
    home = "5 BHK"

    def showProperties(self):
        print(f"Vehicle of {self.name}:", self.vehicle)
        print(f"Profession of {self.name}:", self.profession)
        print(f"Home of {self.name}:", self.home)
        print(f"Hobby of {self.name}:", self.hobby)

class Mother():
    hobby = "Trekking"
    profession = "Teacher"

class Child1(Father, Mother):
    pass

class Child2(Mother, Father):
    pass

# Diamond Problem
# class GrandChild(Child1, Child2):
#     pass

c1 = Child1()
c1.name = "Anuj"
# c1.showProperties()

c2 = Child2()
c2.name = "Neepa"
# c2.showProperties()

# gc1 = GrandChild()
# gc1.showProperties()
