# Ask user for a number
n = int(input("Enter the number: "))

# Loop from 1 to 10
for i in range(1, 11):
    # Print multiplication table using f-string
    print(f"{n} x {i} = {n*i}")
