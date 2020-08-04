def sol(i, arr):
	visit	= [0] * len(arr)
	queue	= [i]

	while queue:
		idx = queue.pop()
		for i, val in enumerate(arr[idx]):
			if visit[i] == 0 and val == 1:
				visit[i] = 1
				queue.append(i)
	return visit

def main():
	n = int(input())
	arr = []
	for i in range(n):
		arr.append(list(map(int, input().split())))

	for i in range(n):
		print(' '.join(map(str, sol(i, arr))))

if __name__ == "__main__":
	main()