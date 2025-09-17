# n=int(input("Enter a number: "))

# def fin_pos_neg():
#     if n>0:
#         print("The number is positive")
#     elif n<0:
#         print("The number is negative")
#     else:
#         print("The number is zero")
# fin_pos_neg()
n=int(input("Enter a number: "))
def fin_fizz_buzz():
    if n%3 ==0 and n%5==0 :
        print("buzzfizz")
    elif n%5==0:
        print("buzz")
    elif n%3==0:
        print("fizz")
    else:
        print(n)

fin_fizz_buzz()


    
