file = open("input.txt")

numbers = file.readline().rstrip().split(",")
boards = [board.split() for board in file.read().split("\n\n")]

def checkRow(board, index):
	for i in range(5):
		if (board[(index * 5) + i] != 'X'):
			return False
	return True

def checkCol(board, index):
	for i in range(5):
		if (board[(i * 5) + index] != 'X'):
			return False
	return True

def checkDiag(board):
	retval = True
	
	for i in range(5):
		if (board[(i * 5) + i] != 'X'):
			retval = False
			break
			
	for i in range(5):
		if (board[(i * 5) + (4 - i)] != 'X'):
			retval = False
			break
			
	return retval
		
def findPuzzle():
	for number in numbers:
		for i in range(len(boards)):
			for x in range(25):
				if (boards[i][x] == number):
					boards[i][x] = 'X'
					if (checkRow(boards[i], int(x / 5)) or checkCol(boards[i], x % 5) or checkDiag(boards[i])):
						return [boards[i], int(number)]
					break

[answer, number] = findPuzzle()

sum = 0
for entry in answer:
	if (entry != 'X'):
		sum += int(entry)

print("Sum of unmarked numbers is:", sum, "\nNumber that was called is:", number, "\nTheir product is: ", (sum * number))
file.close