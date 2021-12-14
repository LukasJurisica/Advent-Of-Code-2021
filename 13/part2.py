file = open("input.txt")

lines = [line.rstrip() for line in file]
i = lines.index("")
dots = [list(map(int, line.split(","))) for line in lines[:i]]
instructions = [[0 if line[11] == "x" else 1, int(line[13:])] for line in lines[i+1:]]
result = set()
m = [0, 0]

for dot in dots:
	for axis, value in instructions:
		if (dot[axis] > value):
			dot[axis] = value - (dot[axis] - value)
	result.add((dot[0] << 32) + dot[1])
	for i in range(2):
		m[i] = max(m[i], dot[i])

for y in range(m[1] + 1):
	for x in range(m[0] + 1):
		print("#" if (x << 32) + y in result else ".", end="")
	print("")
file.close()