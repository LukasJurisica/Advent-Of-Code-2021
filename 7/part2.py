file = open("input.txt")

def fuel(x):
	return x * (x + 1) // 2

numbers = [int(num) for num in file.readline().split(",")]
mean = sum(numbers) // len(numbers)
fuelCost = min([sum([fuel(abs(n - p)) for n in numbers]) for p in [mean, mean + 1]])
	
print("It would take", fuelCost, "units of fuel to align the position")
file.close()