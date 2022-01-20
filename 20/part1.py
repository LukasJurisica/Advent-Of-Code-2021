file = open("input.txt")

algo = [1 if c == '#' else 0 for c in file.readline().rstrip()]
next(file)
inp = [line.rstrip() for line in file.readlines()]
width = len(inp[0])
height = len(inp)
pixels = [[1 if inp[y][x] == '#' else 0 for x in range(width)] for y in range(height)]
void = 0

def getPixel(x, y):
	if (x < 0 or x+1 >= width or y < 0 or y+1 >= height):
		return void
	return pixels[y][x]
	
def convolve(x, y):
	value = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			value |= getPixel(x + j, y + i) << (4 - (i * 3 + j))
	return value

for _ in range(2):
	width += 2
	height += 2
	for i in range(len(pixels)):
		pixels[i].insert(0, void)
		pixels[i].append(void)
	pixels.insert(0, [void] * width)
	pixels.append([void] * width)
	
	temp = [[void for _ in range(width)] for _ in range(height)]
	for y in range(height):
		for x in range(width):
			temp[y][x] = algo[convolve(x, y)]
	pixels = temp
	void = algo[void * 511]

print("The number of pixels that are lit is:", sum([sum(row) for row in pixels]))

file.close()