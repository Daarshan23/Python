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

