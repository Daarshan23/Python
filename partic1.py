#while-else : break-else
#if
#else
n= int(input("n : "))
i = 2
while i < n:
    if n % i == 0:
        print(f"Not prime because its divisble by {i}")
        break
    i+=1
else:
    print("prime.")
    