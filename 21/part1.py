file = open("input.txt")

position = [int(line.rstrip()[28:]) - 1 for line in file]
score = [0, 0]
count = 0
die = 0

turn = 1
while (score[turn] < 1000):
	turn = 1 - turn
	roll = 0
	for i in range(3):
		die = 1 if (die == 100) else (die + 1)
		roll += die
		count += 1
	position[turn] = (position[turn] + roll) % 10
	score[turn] += position[turn] + 1
	
print("The product of the score of the losing player and the number of times the die was rolled is:", score[1 - turn] * count)
	
file.close()