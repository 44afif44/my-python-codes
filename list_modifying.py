'''takes number and converts to list, removes duplicates and sorts in descending order
'''

a=input("enter a numbrer : ")
as_list=a.split()
as_list_2=[]
for x in as_list:
    as_list_2.append(int(x))
as_list_3=[]
for y in as_list_2:
    if y not in as_list_3:
        as_list_3.append(y)
as_list_3.sort(reverse=True)

print(as_list_3)