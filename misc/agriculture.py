def rectSum(rx, ry, x, y, arr):
	ret = 0

	yRange = range(y, ry, -1)
	if y <= ry: yRange = range(y, ry+1, 1)

	xRange = range(x, rx, -1)
	if x <= rx: xRange = range(x, rx+1, 1)

	for i in yRange:
		for j in xRange:
			ret += arr[i][j]
	
	return ret	

def main():
	n = int(input())
	field	= []
	ret		= 0
	for _ in range(n):
		field.append(list(map(int, input().split())))

	for ry in range(n-1):
		for rx in range(n-1):
			leftTop, rightTop = dict(), dict()
			for y in range(n):
				for x in range(n):
					val = rectSum(rx, ry, x, y, field)
					if y <= ry:
						if x <= rx:
							memo = leftTop
						else:
							memo = rightTop
						if val in memo:
							memo[val] += 1
						else:
							memo[val] = 1
					else:
						if x <= rx:
							if val in rightTop:
								ret += rightTop[val]
						else:
							if val in leftTop:
								ret += leftTop[val]
	print(ret)

if __name__ == "__main__":
	main()
