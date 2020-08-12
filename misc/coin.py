def main():
	n, k = list(map(int, input().split()))
	coins = []
	for _ in range(n):
		val = int(input())
		if val > k:
			continue
		coins.append(val)
	
	ret = 0
	while k != 0:
		coin = coins.pop()
		ret += k // coin
		k = k % coin
	print(ret)

if __name__ == "__main__":
	main()
