def search(arr, path, memo={}):
	best = (None, None, 0)

	for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		next_y, next_x = path[-1][0] + direction[0], path[-1][1] + direction[1]
		
		if not ((0 <= next_y <= len(arr)) and (0 <= next_x <= len(arr))) or (next_y, next_x) in path:
			continue

		if (next_y, next_x) in memo:
			best = best if best[2] >= memo[(next_y, next_x)] else (next_y, next_x, memo[(next_y, next_x)]
			continue
		
		future = search(arr, path+[(next_y, next_x)], memo)
		best = best if best[2] > future else (next_y, next_x, future)

	if best == (None, None, 0):
		return 0

	return 1+best[2]
		

def main():
	n = int(input())
	bamboos = []
	for _ in range(n):
		bamboos.append(list(map(int, input().split())))

	memo = dict()	

	for y in range(n):
		for x in range(n):
			path = [(y, x)]
			while path:
				start = path.pop()
				for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
					if start


if __name__ == '__main__':
	main()
