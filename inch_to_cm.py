def inch_to_cm(inch):
    cm=inch * 2.54
    return cm
h=int(input("enter value in inches: "))
print(f"{inch}  inches = {inch_to_cm(h)} cm")
