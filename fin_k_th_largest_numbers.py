'''-finding k th largest numbers for any give numbers-.
cautions : given numbers should be separated by space only.
'''
n=input("enter your numbers : ")
list=n.split()
list_2=[]
for i in list:
    list_2.append(int(i))
list_2.sort(reverse=True)
print(f"the sorted list in descending order is : {list_2}")
k=int(input("enter k th largest number you want : "))
print(list_2[k-1])

