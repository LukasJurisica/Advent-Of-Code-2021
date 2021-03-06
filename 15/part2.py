import heapq

file = open("input.txt")
grid = [[int(i) for i in line.rstrip()] for line in file]
tile_size = len(grid)
size = tile_size * 5
dist = [[(size * size * 9) for _ in range(size)] for _ in range(size)]

hq = [(0,0,0)]
while (len(hq) > 0):
	r, x, y = heapq.heappop(hq)
	risk = grid[y % tile_size][x % tile_size] + (y // tile_size) + (x // tile_size) - 1
	risk = (risk % 9) + r + 1

	if risk < dist[y][x]:
		dist[y][x] = risk

		if y + 1 == size and x + 1 == size:
			print("The lowest total risk of any path from the top left to the bottom right is:", risk - grid[0][0])
			break

		for dx, dy in [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]:
			if dx >= 0 and dx < size and dy >= 0 and dy < size:
				heapq.heappush(hq, (risk, dx, dy))