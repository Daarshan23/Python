party = {
    "Vivek" : "Pizza",
    "Ayush" : 23,
    "Jay" : ["Soup", "Main Course", "Gulab Jamun"],
    "Rishi" : ("Dosa", "Pepsi"),
    "Alakh" : {"Dosa", "Pepsi"},
    "Dhiraj" : frozenset({"Rotlo", "Gud", "Buttermilk"}),
    "Marlin" : {"BF" : "Sandwich", "Lunch" : "Punjabi", "Dinner" : "Pau Bhaji"}
}
#take a name of the person from user as input and prinnt their dish as output
# i = input("Enter the name of the person: ").capitalize()
# print(party[i])

# name = input("Enter a name: ").capitalize()
# dish = party.get(name)
# if dish is not None:
#     print(f"{name}'s dish is {dish}.")
# else:
#     print(f"No dish found for {name}.")

#print one by one dish



# for name in party:
#     dish = party[name]
#     if dish is not None:
#         print(f"{name}'s dish is {dish}.")
#     else:
#         print(f"No dish found for {name}.")

# name = input("Enter a name: ")
# dish = party.get(name)
# if dish is not None:
#     if isinstance(dish, (list, tuple, set, frozenset)):
#         print(f"{name}'s dishes are:")
#         for item in dish:
#             print(item)
#     elif isinstance(dish, dict):
#         print(f"{name}'s dishes are:")
#         for key, value in dish.items():
#             print(f"{key}: {value}")
#     else:
#         print(f"{name}'s dish is {dish}.")
# else:
#     print(f"No dish found for {name}.")

#print dish one by one of one person
# for name in party:

#take name of the person from user as input and print theri dish but in marlin ask their meal




    
# name = input("Enter a name: ")
# if name == "Marlin":
#     meal = input("Enter a meal (BF, Lunch, or Dinner): ")
#     dish = party.get(name, {}).get(meal)
#     if dish is not None:
#         print(f"{name}'s {meal} dish is {dish}.")
#     else:
#         print(f"No {meal} dish found for {name}.")


# consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh"]

# #create dicitonary of consumer and value will be 1000

# consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh"]
# consumer_dict = {consumer: 1000 for consumer in consumers}
# print(consumer_dict)

#create dicitonary of consumer and key is name and value will be 1000
consumer_dict = {}
consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh","Vivek"]
for consumer in consumers:
    consumer_dict[consumer] = 1000
print(consumer_dict)