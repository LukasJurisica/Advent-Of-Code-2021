file = open("input.txt")

state = [list(map(int, line.rstrip())) for line in file]
flash = []

def getCoords(x, y):
	coords = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			dy = y + i
			dx = x + j
			if (dx >= 0 and dx < 10 and dy >= 0 and dy < 10 and (i != 0 or j != 0)):
				coords.append([dx, dy])
	return coords
	
def incrementState(x, y, flag):
	if (state[y][x] == 9):
		flash.append([x, y])
		state[y][x] = 0
	elif (flag or state[dy][dx] != 0):
		state[y][x] += 1

count = 0
while True:
	flash = []
	for y in range(10):
		for x in range(10):
			incrementState(x, y, True)
	
	f = 0
	while(f < len(flash)):
		for dx, dy in getCoords(flash[f][0], flash[f][1]):
			incrementState(dx, dy, False)
		f += 1

	count += 1
	if (len(flash) == 100):
		break

print("The first step during which all octopuses flash is", count)
file.close()