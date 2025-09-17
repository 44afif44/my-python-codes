num=int(input("enter the number the of students of ur class: "))
student=[]
for i in  range(num):
    name=input("enter the name of that student : ")
    mark=int(input("enter the marks of that student : "))
    if mark>= 80:
        grade="A+"
    elif mark>=70:
        grade ="A"
    elif mark >=60:
        grade ="A-"
    elif mark  >=50:
        grade ="B"
    else :
        grade="F"
    student.append((name,mark,grade))
print("\n......details of students......")

for x in student:

    print(f"name={x[0]},mark={x[1]},grade={x[2]}")

