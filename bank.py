"""
9. Royal Bank App

Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

def login(username,password):
    login_username=input("Enter Username to login your account:")
    login_password=input("Enter Password:")
    if username == login_username and password == login_password:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

username=input("Enter Username:")
password=input("Enter password:")
balance=25000
print("Account opened successfully.")
print(f"Your balance is {balance}.")

if login(username,password)==True:
    print("Enter your choice:")
    print("1. Deposit \n2. Withdraw \n3. Check Balance \n4. Log out")
    choice=int(input(""))
    if choice==1:
        print("Deposit")
        print(f"Your account have {balance}Rs.")
        dp_amount=int(input("Input Deposit amount:"))
        balance +=dp_amount
        print(f"Now your Current Balance is {balance}")
        pass
    elif choice==2:
        print("Withdraw")
        print(f"Withdraw")
        pass
    elif choice==3:
        # Check Balance
        pass
    elif choice==4:
        # Log out
        pass

"""
def sqrt(n):
    return n ** 0.5
myList = [16,25,36,49,81]

# write your code here
sqrtList=[sqrt(i) for i in myList]

print(sqrtList)
# o/p: [4.0, 5.0, 6.0, 7.0, 9.0]
"""
"""
-----------------------------------------------------------------------------------------------------------------------------
# Write a function to calculate factorial of an integer here
def fact(n):
    mul=1
    for i in range(1,n+1):
        mul*=i
    return mul
yourList = [2,3,4,5,6,7,8]

# Write your code using that factorial function & map here
    
# factList=[fact(i) for i in yourList]
factList=list(map(fact,yourList))

print(factList)
# o/p: [2, 6, 24, 120, 720, 5040, 40320]
"""
# Write a function here, that returns True or False based on whether the number given in its argument is Prime or not.
def isPrimeNum(n):
    i=1
    count = 0
    while i <= n:
        if n%i == 0:
            count += 1
        i +=1
    if count == 2:
        return True
    else:
        return Falseq
num_list = [x for x in range(55, 155)]

# Write additional code here that uses that function
primeList=[]
# primeList=list(map        (isPrimeNum,num_list))
for i in num_list:
    if isPrimeNum(i):
        primeList.append(i)

print(primeList)
# output list must have only prime numbers from 55 to 154