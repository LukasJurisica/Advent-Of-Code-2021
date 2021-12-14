file = open("input.txt")

token = file.readline().rstrip()
next(file)

count = {}
pairs = {}
rules = {}
steps = 40

for line in file:
	i, o = line.rstrip().split(" -> ")
	rules[i] = o
	pairs[i] = 0
	count[o] = 0

for i in range(len(token)):
	count[token[i]] += 1
	if (i + 1 < len(token)):
		pairs[token[i:i+2]] += 1

for i in range(steps):
	toBeAdded = []
	for key, value in pairs.items():
		if (value > 0):
			toBeAdded.append([key, rules[key], value])
			pairs[key] = 0
	
	for a, b, c in toBeAdded:
		pairs[a[0] + b] += c
		pairs[b + a[1]] += c
		count[b] += c

print("If you take the quantity of the most common element and subtract the quantity of the least common element, you get", max(count.values()) - min(count.values()))
file.close()