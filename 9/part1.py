file = open("input.txt")
terrain = [line.rstrip() for line in file.readlines()]
height = len(terrain)
width = len(terrain[0])

def getCoords(x, y):
	l = []
	if (y >        0): l.append([ x ,y-1])
	if (x < width -1): l.append([x+1, y ])
	if (y < height-1): l.append([ x ,y+1])
	if (x >        0): l.append([x-1, y ])
	return l

def checkLowPoint(x, y):
	curr = int(terrain[y][x])
	for dx, dy in getCoords(x, y):
		if (int(terrain[dy][dx]) <= curr):
			return 0
	return curr + 1

count = 0
for y in range(height):
	for x in range(width):
		count += checkLowPoint(x, y)

print("The sum of the risk levels of all low points on the heightmap is", count)
file.close()