file = open("input.txt")

count = 0
for line in file:
	inp, out = [entry.split(" ") for entry in line.rstrip().split(" | ")]
	inp = sorted(inp, key=len)
	
	number = ""
	for item in out:
		s = set(item)
		l = len(item)
		a = len(s & set(inp[0]))
		b = len(s & set(inp[2]))
		
		if   (l == 2): number += "1"
		elif (l == 3): number += "7"
		elif (l == 4): number += "4"
		elif (l == 5): number += "3" if a==2 else ("2" if b==2 else "5")
		elif (l == 6): number += "6" if a==1 else ("0" if b==3 else "9")
		elif (l == 7): number += "8"
		
	count += int(number)

print("The result of adding all the output values is", count)
file.close()