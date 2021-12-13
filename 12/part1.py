file = open("input.txt")

dict = {}
paths = [["start"]]
count = 0

for line in file:
	a, b = line.rstrip().split("-")
	if (a not in dict): dict[a] = []
	if (b not in dict): dict[b] = []
	dict[a].append(b)
	dict[b].append(a)
	
while(True):
	newPaths = []
	for path in paths:
		for node in dict[path[-1]]:
			if (node == "end"):
				count += 1
			elif node.isupper() or node not in path:
				newPaths.append(path + [node])
	if (len(newPaths) == 0):
		break
	paths = newPaths

print("There are", count, "paths through the cave system")
file.close()