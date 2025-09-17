n=int(input("Enter a natural number: "))
for i in range  (1,n+1):
     if (i==1 or i==n):
          print("*"*n)
     else:
          print("*",end="")
          print(" "*(n-2),end="")
          print("*", end="")#if we dont use end="", it will print a new line and ther will be 2 gaps between the lines.
          print(" ") 
     
          
     

    
     

