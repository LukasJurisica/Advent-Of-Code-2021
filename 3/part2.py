file = open("input.txt")

numDigits = 12
lines = [line.rstrip() for line in file]
options = ['1', '0']

def calc(values, index):
	count = 0
	for i in range(numDigits):
		half = len(values) / 2
		for value in values:
			if (value[i] == '1'):
				count += 1
	
		values = list(filter(lambda v: v[i] == (options[index] if (count >= half) else options[1 - index]), values))
		
		if (len(values) == 1):
			break
		
		count = 0
	
	value = values[0][::-1]
	result = 0
	
	for i in range(numDigits):
		result += int(value[i]) * pow(2, i)
	return result

oxy = calc(lines, 0)
co2 = calc(lines, 1)

print("Oxygen is:", oxy, "\nCO2 is:", co2, "\nTheir product is: ", (oxy * co2))
file.close