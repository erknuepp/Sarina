
# number = int(input("Enter a number:"))

# index = 1

# while index < 11:
#     # print(str(index), " * ", str(number), " = ", str(index * number))
#     print("{} * {} = {}".format(index, number, index*number))
#     index = index + 1


min = 999999
max = -999999
i = 0

for z in range(1, 11):
    number = int(input("Enter a number: "))
    if number < min:
        min = number

    if number > max:
        max = number

    if number % 3 == 0:
        i = i + 1

print("Min:", min)
print("Max:", max)
print("Number divisible by three:", i)
