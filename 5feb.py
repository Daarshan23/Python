#write a program that takes name of a fruit from user and print whether it is in the followinf list or not.

l1=["blueberry","banana","kiwi","mango","grapes"]
fruit=input("Enter fruit : ")
if(fruit in l1):
    print(fruit,"Is list")
else:
    print(fruit,"Is Not in list")