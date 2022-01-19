file = open("input.txt")

scanners = [[[int(c) for c in b.split(",")] for b in beacons.split("\n")[1:]] for beacons in file.read().split("\n\n")]
positions = [[0, 0, 0]]
matches = [0]

def orient(x, y, z, up, ro):
	# No rotation necesary when up == 0
	if   (up == 1): y, z = -z, y # Rotation of  90 around x
	elif (up == 2): y, z = -y,-z # Rotation of 180 around x
	elif (up == 3): y, z =  z,-y # Rotation of 270 around x
	elif (up == 4): x, y = -y, x # Rotation of  90 around z
	elif (up == 5): x, y =  y,-x # Rotation of 270 around z
	# No rotation necesary when ro == 0
	if   (ro == 1): x, z =  z,-x # Rotation of  90 around y
	elif (ro == 2): x, z = -x,-z # Rotation of 180 around y
	elif (ro == 3): x, z = -z, x # Rotation of 270 around y
	return [x, y, z]
	
def CheckMatch(a, b):
	for up in range(6):
		for ro in range(4):
			oriented = [orient(x, y, z, up, ro) for [x, y, z] in scanners[b]]
			
			for ax, ay, az in scanners[a]:
				for bx, by, bz in oriented:
					[ox, oy, oz] = [ax-bx, ay-by, az-bz]
					offsetted = [[x+ox, y+oy, z+oz] for [x, y, z] in oriented]
				
					count = 0
					for entry in offsetted:
						if entry in scanners[a]:
							count += 1
					if (count >= 12):
						scanners[b] = offsetted
						positions.append([ox, oy, oz])
						return True
	
	return False
				

for a in matches:
	for b in range(len(scanners)):
		if (b in matches):
			continue
		
		if (CheckMatch(a, b)):
			matches.append(b)

dist = 0
for [ax, ay, az] in positions:
	for [bx, by, bz] in positions:
		dx, dy, dz = abs(bx-ax), abs(by-ay), abs(bz-az)
		dist = max(dx+dy+dz, dist)

print("The largest manhattan distance between any 2 scanners is:", dist)

file.close()