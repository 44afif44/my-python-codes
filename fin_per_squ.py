import math
n=int(input("enter a number"))
def fin_per_sqr():


    a=math.sqrt(n)
    b=a.is_integer()
# x=type(a)
# print(x)
    if b== True :
        print("its a perfect square")
    else:
        print("its not a perfect square")
    
fin_per_sqr()