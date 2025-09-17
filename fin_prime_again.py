n=int(input("enter a number"))
def fin_prime():
    if n<2:
        print("its not a prime number")
    for i in range(2,n+1):
        if(n%i==0):

            print("its not prime number")
            break
    else:
        print("prime number")

fin_prime()            
