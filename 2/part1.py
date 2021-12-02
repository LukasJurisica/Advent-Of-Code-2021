file = open("input.txt")

depth = 0
hpos = 0

for line in file:
	command = line.rstrip().split(" ")
	if (command[0] == "forward"):
		hpos += int(command[1])
	elif (command[0] == "down"):
		depth += int(command[1])
	elif (command[0] == "up"):
		depth -= int(command[1])

print("Depth is:", depth, "\nHorizontal Position is:", hpos, "\nTheir product is: ", (hpos * depth))
file.close