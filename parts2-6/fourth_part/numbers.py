for number in  list(range(0,21)):
	print(number)
#for number in  range(0,1000000):
#	print(number)
numbers =list(range(0,1000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
for number in  list(range(1,20,2)):
	print(number)
for number in  list(range(3,30,3)):
	print(number)
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)
cubes = [value**3 for value in range(1,11)]
print(cubes)
