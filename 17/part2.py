file = open("input.txt")
line = file.readline().rstrip()
target = [[int(n) for n in pair.split("..")] for pair in line[15:].split(", y=")]
xRange = [0, target[0][1]]
yRange = [target[1][0], -(target[1][0] + 1)]

r = 0
while(r < target[0][0]):
	xRange[0] += 1
	r += xRange[0]
	
count = 0
for x in range(xRange[0], xRange[1] + 1):
	for y in range(yRange[0], yRange[1] + 1):
		pos = [0, 0]
		vel = [x, y]
		while (pos[0] <= target[0][1] and pos[1] >= target[1][0]):
			if (pos[0] >= target[0][0] and pos[1] <= target[1][1]):
				count += 1
				break
			pos[0] += vel[0]
			pos[1] += vel[1]
			if (vel[0] > 0): vel[0] -= 1
			vel[1] -= 1

print("There number of distinct initial velocity values that cause the probe to be within the target area is:", count)
file.close()