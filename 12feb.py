#for-else
n = int (input("n : "))
for i in range (2,n):
    if n % i == 0:
        print("not primme.")
        break
else:
    print("prime")