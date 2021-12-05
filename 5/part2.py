file = open("input.txt")
dict = {}

def sign(a):
	return 1 if a>0 else -1 if a<0 else 0

for line in file:
	p = [int(coord) for coord in line.rstrip().replace(" -> ", ",").split(",")]
	
	d = [p[2] - p[0], p[3] - p[1]]
	s = [sign(d[0]), sign(d[1])]
	r = abs(d[0]) if (d[1] == 0) else abs(d[1])
	
	for i in range(r + 1):
		coord = ((i * s[0] + p[0]) << 16) + (i * s[1] + p[1])
		if coord in dict:
			dict[coord] += 1
		else:
			dict[coord] = 1
			
count = 0				
for item in dict.values():
	if item >= 2:
		count += 1

print("The number of points where 2 lines overlap is:", count)
file.close