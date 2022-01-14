file = open("input.txt")

def loadLine(line):
	result = []
	side = []
	for c in line:
		if (c == "["):
			side.append(0)
		elif (c == "]"):
			side.pop()
		elif (c == ","):
			side[-1] = 1
		else:
			result.append([int(c), side.copy()])
	return result
	
def add(a, b):
	for i in range(len(a)):
		a[i][1].insert(0, 0)
	for i in range(len(b)):
		b[i][1].insert(0, 1)

	result = a + b
	
	def explode(i):
		if (i > 0):
			result[i-1][0] += result[i][0]
		if (i+2 < len(result)):
			result[i+2][0] += result[i+1][0]
		result[i] = [0, result[i][1][:-1]]
		result.pop(i+1)
		
	def mitosis(i):
		value, side = result[i]
		half = value//2
		result[i] = [half, side + [0]]
		ceiling = half if value%2 == 0 else half+1
		result.insert(i+1, [ceiling, side + [1]])

	i = 0
	while (i < len(result)):
		if (len(result[i][1]) == 5):
			explode(i)
		i += 1
			
	i = 0
	while (i < len(result)):
		if (result[i][0] > 9):
			mitosis(i)
			if (len(result[i][1]) == 5):
				explode(i)
				i = max(i-1, 0)
		else:
			i += 1

	return result
	
def calculateMagnitude(num):
	total = 0
	for value, side in num:
		for s in side:
			value *= [3, 2][s]
		total += value
	return total

num = loadLine(file.readline().rstrip())
for line in file:
	num = add(num, loadLine(line.rstrip()))

print("The magnitude of the final sum is:", calculateMagnitude(num))

file.close()
