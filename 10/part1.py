file = open("input.txt")

openBrace  = ["(", "[", "{", "<"]
closeBrace = [")", "]", "}", ">"]
errorValue = [3, 57, 1197, 25137]

stack = []
count = 0
for line in file:
	for char in line.rstrip():
		if char in openBrace:
			stack += char
		else:
			i = closeBrace.index(char)
			if stack[-1] == openBrace[i]:
				stack.pop()
			else:
				count += errorValue[i]
				break
				
print("The total syntax error score is", count)
file.close()