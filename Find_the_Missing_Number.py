'''Find the missing number from a list of numbers ranging from any 0 to n'''

enter=input("enter your numbers : ")
list_1=enter.split()
list_2=[]
for i in list_1:
    list_2.append(int(i))
summation=sum(list_2)
n=len(list_2)
total=n*(n+1)/2




# summation=sum(list_2)
# maxi=max(list_2)
# mini=min(list_2)
# total=0
# for i in range(mini,maxi+1):
#     total+=i
missing_number=total-summation
print("the missing number is : ",missing_number)
  