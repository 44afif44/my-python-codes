vowels = "aeiouAEIOU"
n=input("Enter a string: ")
def fin_vow():
    counte=0
    for letter in n:
         
        if letter in vowels:
            counte+=1
    if counte>=1:
            
            print(f"there is a vowel in the string...{counte} ")
            
    else:
        print("No vowel in the string")
fin_vow()

