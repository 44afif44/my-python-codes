def add(l,word):
    n=[]
    for iteam in l:
        if (iteam !=word):
            n.append(iteam.strip(word))
    return n
l=['apple', 'banana', 'pcherry', 'apple']
print(add(l,'apple'))

   
   