def fin_miss(numbers):
    n=len(numbers)+1
    for i in range (1,n+1):
        if i not in numbers:
            return i
numbers=[2,3,4,5,6,8]
print(fin_miss(numbers))
    