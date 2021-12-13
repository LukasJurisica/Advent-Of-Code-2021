file = open("input.txt")

dict = {}
paths = [[True, "start"]]
count = 0

for line in file:
	a, b = line.rstrip().split("-")
	if (a not in dict): dict[a] = []
	if (b not in dict): dict[b] = []
	if (b != "start"): dict[a].append(b)
	if (a != "start"): dict[b].append(a)
	
while(True):
	newPaths = []
	for path in paths:
		for node in dict[path[-1]]:
			if (node == "end"):
				count += 1
			elif (node.isupper() or node not in path):
				newPaths.append(path + [node])
			elif (path[0]):
				newPaths.append([False] + path[1:] + [node])
				
	if (len(newPaths) == 0):
		break
	paths = newPaths

print("There are", count, "paths through the cave system")
file.close()