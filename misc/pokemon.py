def main():
	n, m = list(map(int, input().split()))

	name = []
	nameIdx = dict()
	
	for idx in range(n):
		val = input()
		name.append(val)
		nameIdx[val] = idx+1
		
	ret = []

	for _ in range(m):
		q = input()
		if q.isdigit():
			ret.append(name[int(q)-1])
			continue
		ret.append(nameIdx[q])

	for r in ret:
		print(r)

if __name__ == '__main__':
	main()
