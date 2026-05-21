numbers = []
cubes =[]

number = 5
while number <= 100:
    numbers.append(number)
    number += 5

for number in numbers:
    number = number **3
    cubes.append(number)

print(numbers)
print(cubes)

