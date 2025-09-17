write=input("enter something : ")
write=write.replace(',',' ')
write=write.replace('.',' ')
words=write.split()
list_1=[]
for i in words:
    list_1.append(i)
dic={}
for items in list_1:
    if items in dic:
        dic[items]+=1
    else:
        dic[items]=1
print(dic)
    

