#
# Prime number:

n = int(input("Please enter your input number: "))
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("%d is a Not Prime."%n)
            break
    else:
        print("%d is a Prime."%n)
else:
    print("%d is a Not Prime."%n)
    
# Use to Definition Function:

'''
def Prime_number_chcek(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                return ("%d is a Not Prime."%n)
        return ("%d is a Prime."%n)
    return ("%d is a Not Prime."%n)

# Main Driver:
if __name__=="__main__":
    n = int(input("Enter your input number: "))
    print(Prime_number_chcek(n))
'''