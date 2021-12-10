file = open("input.txt")

openBrace  = ["(", "[", "{", "<"]
closeBrace = [")", "]", "}", ">"]

def isIncomplete(line):
	stack = []
	
	for char in line:
		if char in openBrace:
			stack += char
		else:
			i = closeBrace.index(char)
			if stack[-1] == openBrace[i]:
				stack.pop()
			else:
				return [], False
	
	return stack, True

scores = []
for line in file:
	stack, incomplete = isIncomplete(line.rstrip())	
	if (incomplete):
		score = 0
		for char in stack[::-1]:
			i = openBrace.index(char)
			score = (score * 5) + i + 1
		scores.append(score)

scores.sort()				
print("The middle autocomplete score is", scores[len(scores) // 2])
file.close()