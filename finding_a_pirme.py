n=int(input("enter a number: "))
if n==1 or n==0:
    print("its not a prime number :")
for i in range(2, n):
    if n % i == 0:
        print("its not a prime number :")
        break
else:
    print("its a prime number :")