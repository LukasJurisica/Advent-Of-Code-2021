file = open("input.txt")
numDigits = len(file.readline().rstrip())
file.seek(0)

count = [0] * numDigits
total = 0

file.seek(0)

for line in file:
	line = line.rstrip()
	for i in range(numDigits):
		if (line[i] == '1'):
			count[i] += 1
	total += 1
		
half = total / 2
gamma = 0
epsilon = 0

for i in range(numDigits):
	if (count[-(i + 1)] > half):
		gamma += pow(2, i)
	else:
		epsilon += pow(2, i)

print("Gamma is:", gamma, "\nepsilon is:", epsilon, "\nTheir product is: ", (gamma * epsilon))
file.close