def factorial(n):
    if n==0 or n==1:
        return 1
    return (n*factorial(n-1))
n=int(input("Enter a number: "))
print(f"the fucking fatorial is:{factorial(n)}")

'''return statement is used to store a value to the main function and
it can be used to call it later.


'''