file = open("input.txt")
line = file.readline().rstrip()
velocity = -int(line[line.index("y=")+2:].split("..")[0]) - 1
print("The highest y position it reaches on this trajectory is:", velocity * (velocity + 1) // 2)
file.close()
