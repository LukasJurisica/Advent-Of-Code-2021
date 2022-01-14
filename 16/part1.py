file = open("input.txt")
s = bin(int("1" + file.readline(), 16))[3:]
total = 0
offset = 0

while True:
	version = int(s[offset : offset+3], 2)
	total += version
	typeID = int(s[offset+3 : offset+6], 2)
	offset += 6

	if (typeID == 4):
		while s[offset] == "1":
			offset += 5
		offset += 5
	else:
		if (s[offset] == "0"): # next 15 bits represents the total length of the sub-packets
			offset += 16
		else: # next 11 bits represents the number of sub-packets
			offset += 12

	rem = s[offset:]
	if (rem == len(rem) * rem[0]):
		break

print("The sum of all the version numbers is:", total)