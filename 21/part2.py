file = open("input.txt")

def encrypt(key):
	result = 0
	for i in range(4):
		result |= key[i] << (i * 8)
	return result
	
def decrypt(key):
	result = [0, 0, 0, 0]
	for i in range(4):
		result[i] = (key >> (i * 8)) & 255
	return result

position = [int(line.rstrip()[28:]) - 1 for line in file]
wins = [0, 0]
universes = { encrypt([position[0], position[1], 0, 0]): 1 }
rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
			
turn = 0
while (len(universes) > 0):
	nextState = {}
	for universe, instances in universes.items():
		universe = decrypt(universe)
		for roll, count in rolls.items():
			n = universe.copy()
			n[turn] = (n[turn] + roll) % 10
			n[turn+2] += n[turn] + 1
			en = encrypt(n)
			if (n[turn+2] >= 21):
				wins[turn] += instances * count
			elif (en in nextState):
				nextState[en] += instances * count
			else:
				nextState[en] = instances * count
	turn = 1 - turn
	universes = nextState
	
print("The number of universes the player won in is:", max(wins))

file.close()