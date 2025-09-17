def rem(l,word):
    for item in l:
        l.remove(word)
        return l
l=['apple', 'banana', 'cherry', 'apple']
print(rem(l,'apple'))