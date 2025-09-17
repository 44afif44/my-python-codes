vowels="aeiouAEIOU"
def count_vow(n):
    count=0
    for i in  vowels:
        if i in n:
            count+= 1
            # print("there are vowels")
    if count>0:
            
            print("there are vowels")
    else:
        print("therre are no vowels")
    print(f"the numbers of vowels {count}")
        # else:
        #     print("there are no vowels")
        # break
    # a=n.count(vowels)
    # print(f"the number of vowels are {a}")
count_vow("afffiou")

    