file = open("input.txt")

count = 0
for line in file:
	line = line.rstrip().split(" | ")[1].split(" ")
	count += sum(len(item) in [2, 3, 4, 7] for item in line)
	
print("The digits 1, 4, 7, and 8 appear", count, "times")
file.close()