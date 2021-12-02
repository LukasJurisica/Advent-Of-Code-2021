file = open("input.txt")

depths = [int(line.rstrip()) for line in file]
count = 0
prev = depths[0] + depths[1] + depths[2]

for i in range(2, len(depths)):
	sum = depths[i] + depths[i - 1] + depths[i - 2]
	if (sum > prev):
		count += 1
	prev = sum

print("Number of increases is: " + count)
file.close