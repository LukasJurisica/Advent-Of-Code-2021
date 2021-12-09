file = open("input.txt")

numbers = [int(num) for num in file.readline().split(",")]
median = sorted(numbers)[(len(numbers) + 1) // 2]
fuelCost = sum([abs(n - median) for n in numbers])
	
print("It would take", fuelCost, "units of fuel to align the position")
file.close()