file = open("input.txt")
terrain = [list(line.rstrip()) for line in file.readlines()]
height = len(terrain)
width = len(terrain[0])

def getCoords(x, y):
	l = []
	if (y >        0): l.append([ x ,y-1])
	if (x < width -1): l.append([x+1, y ])
	if (y < height-1): l.append([ x ,y+1])
	if (x >        0): l.append([x-1, y ])
	return l

def dfs(x, y):
	if (terrain[x][y] == "9"):
		return 0
	terrain[x][y] = "9"
	res = 1
	for dx, dy in getCoords(x, y):
		res += dfs(dx, dy)
	return res

basins = []
for y in range(height):
	for x in range(width):
		s = dfs(x, y)
		if (s != 0):
			basins.append(s)

basins.sort()
print("The product of the 3 largest basins is", basins[-3] * basins[-2] * basins[-1])
file.close()