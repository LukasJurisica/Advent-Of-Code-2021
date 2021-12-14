file = open("input.txt")

lines = [line.rstrip() for line in file]
i = lines.index("")
dots = [list(map(int, line.split(","))) for line in lines[:i]]
instructions = [[0 if line[11] == "x" else 1, int(line[13:])] for line in lines[i+1:]]
result = set()

for dot in dots:
	axis, value = instructions[0]
	if (dot[axis] > value):
		dot[axis] = value - (dot[axis] - value)
	result.add(str(dot))

print(len(result))
file.close()