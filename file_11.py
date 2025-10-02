list_1 = [5, 4, 3, 7, 8, 9]
sum_of_list = 0

for i in list_1:
    sum_of_list = sum_of_list + i

print(sum_of_list)


#Suqares up to n

length = int(input("Enter Length: "))

result = []
for i in range(1, length+1):
    result.append(i * i)

print(f"Squares Up to {length}: {result}")