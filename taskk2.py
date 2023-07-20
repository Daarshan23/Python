
# Functions Examples:
# 1. Write a Python function to find factorial of a number given in its argument. Develop a main program that takes five integers from user and print sum of their factorials using that function.
"""
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
myList=[int(input(f"myList of {i}:")) for i in range(5)]
sum=0
for i in myList:
    sum+=factorial(i)
print(sum)
"""
# 2. Write a Python function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.
"""
def findPrimeNum(n1):
    i=1
    count = 0
    while i <= n1:
        if n1%i == 0:
            # print(i)
            count += 1
        i +=1
    if count == 2:
        print(n1,"is prime number.")
    else:
        print(n1,"is not a prime number.")
number=int(input("Enter A number:"))
findPrimeNum(number)
"""


# 3. Make a Python program that uses a function to find average of 5 given numbers and write Python main program that takes 5 integers from user, uses the factorial function that you have already written in ex-1 to find factorial of each one of them and using average function prints the average of factorials of them.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def avg(n):
    print(sum(n)/5)
myList=[int(input(f"myList of {i}:")) for i in range(5)]
fact_list=[]
for i in myList:
    fact_list.append(factorial(i))
avg(fact_list)

# 4. Make a Python program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
#     ap:
#     first term = a = 5
#     difference = d = 4
#     ap = 5, 9, 13, 17, 21, 25,...
#     nth term = a + (n-1)d
"""
def nth(a, d, n):
    nth_term = a + (n - 1) * d
    return nth_term
# Example usage
a = int(input("first term:"))
d = int(input("difference:"))
n = int(input("nth term:"))
nth_term = nth(a, d, n)
print(nth_term)
"""
# 5. Make a Python program that uses a function to find nth term of an geometric progression whose first term is a & common ratio is r.
"""
def nthOfGeometric(a,r,n):
    nth_term=a*(r**(n-1))
    return nth_term
a = int(input("first term:"))
r = int(input("common ratio:"))
n = int(input("nth term:"))
nth_term=nthOfGeometric(a,r,n)
print(nth_term)
"""
# 6. Make a function that checks whether the given number is a perfect number or not. Make a Python program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.
"""
def perfectCheck(n):
    temp=n
    i=1
    sum=0
    while i < n:
        if n%i == 0:
            sum += i
        i += 1
    if sum == temp:
        return True
    return False
n1=int(input("Enter two numbers :"))
n2=int(input())
while n1<=n2:
    if perfectCheck(n1):
        print(n1)
    n1+=1
"""
# 7. Write a Python function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.
"""
def primeCheck(n):
    i=1
    count = 0
    while i <= n:
        if n%i == 0:
            # print(i)
            count += 1
        i +=1
    if count == 2:
        return True
    else:
        return False
n1=int(input("Enter two numbers :"))
n2=int(input())
while n1<=n2:
    if primeCheck(n1):
        print(n1)
    n1+=1
"""
# 8. Write a Python function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.

"""
def armstrongckeck(no):
    power=len(str(no))
    dup=no
    sum=0
    while dup>0:
        last_digit=dup%10
        sum +=(last_digit**power)
        dup //=10
    if sum== no:
        print(no)
 
n1=int(input("Enter two numbers :"))
n2=int(input())
while n1<=n2:
    armstrongckeck(n1)
    n1+=1   
"""
# numbers = []
# while True:
#     num = input("Enter a number and press q to quit")
#     if num == 'q':
#         break
#     else:
#         numbers.append(float(num))

# avg = sum(numbers) / len(numbers)
# print("avarge:", avg)


# def fun2 (a=10,b=20,*args):
#     pass 

# print(fun2())


