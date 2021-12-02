file = open("input.txt")

depths = [int(line.rstrip()) for line in file]
count = 0

for i in range(1, len(depths)):
	if (depths[i] > depths[i - 1]):
		count += 1

print("Number of increases is: " + count)
file.close