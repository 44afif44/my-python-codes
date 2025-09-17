with open ("file.txt","r")as f:
    lines=f.readlines()
lineno=1
for line in lines:
    
    if "python" in line:
        print(f"there is pythn in line {lineno}")
        break
    lineno+=1
else:

    print("No line contains 'python'")


      