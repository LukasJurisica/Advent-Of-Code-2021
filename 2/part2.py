file = open("input.txt")

depth = 0
hpos = 0
aim = 0

for line in file:
	command = line.rstrip().split(" ")
	if (command[0] == "forward"):
		hpos += int(command[1])
		depth += int(command[1]) * aim
	elif (command[0] == "down"):
		aim += int(command[1])
	elif (command[0] == "up"):
		aim -= int(command[1])

print("Depth is:", depth, "\nHorizontal Position is:", hpos, "\nTheir product is: ", (hpos * depth))
file.close