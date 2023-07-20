#while loop prime numbers in python.
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break
n=int(input("Enter a number : "))