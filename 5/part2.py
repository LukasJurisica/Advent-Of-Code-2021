file = open("input.txt")
dict = {}

def sign(a):
	return 1 if a>0 else -1 if a<0 else 0

def ensureKey(coord):
	if coord in dict:
		dict[coord] += 1
	else:
		dict[coord] = 1

for line in file:
	p = [int(coord) for coord in line.rstrip().replace(" -> ", ",").split(",")]
	
	dx = sign(p[2] - p[0])
	dy = sign(p[3] - p[1])
	
	if (dx == 0):
		for i in range(p[1], p[3] + dy, dy):
			ensureKey((p[0] << 16) + i)
	elif (dy == 0):
		for i in range(p[0], p[2] + dx, dx):
			ensureKey((i << 16) + p[1])
	else:
		for i in range(abs(p[2] - p[0]) + 1):
			ensureKey(((i * dx + p[0]) << 16) + (i * dy + p[1]))
			
count = 0				
for item in dict.values():
	if item >= 2:
		count += 1

print("The number of points where 2 lines overlap is:", count)
file.close