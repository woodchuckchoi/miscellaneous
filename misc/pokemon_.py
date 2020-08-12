def main():
	n, m = list(map(int, input().split()))

	iToN = dict()
	nToI = dict()

	for idx in range(n):
		name = input()
		iToN[idx+1] = name
		nToI[name] = idx+1

	ret = []

	for _ in range(m):
		q = input()
		if q.isdigit():
			ret.append(iToN[int(q)])
			continue
		ret.append(nToI[q])

	for r in ret:
		print(r)

if __name__ == '__main__':
	main()
