file = open("input.txt")

count = [0 for i in range(9)]
numdays = 256

for number in file.readline().rstrip().split(","):
	count[int(number)] += 1
	
for day in range(numdays):
	temp = count[0]

	for i in range(1, 9):
		count[i - 1] = count[i]
	
	count[6] += temp
	count[8] = temp
	
sum = 0
for item in count:
	sum += item

print("There would be", sum, "lanternfish after", numdays, "days.")
file.close