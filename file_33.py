list_2 = [1, 2, 3, 4, 5]

greater = 0

for item in list_2:
    if item > greater:
        greater = item

print("Greater no:", greater)


number = int(input("Enter any number: "))
result = 1

for i in range(1, number+1):
    result = result * i

print(f"Factorial of {number} is: {result}")


n1 = int(input("Enter Any Number: "))

print(f"Square of {n1} is: {n1 * n1}")
