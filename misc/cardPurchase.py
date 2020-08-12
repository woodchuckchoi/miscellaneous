def main():
	n	= int(input())
	arr	= list(map(int, input().split()))
	ret = [[n, 0]]
	maxG= 0

	while ret:
		curN, curVal = ret.pop()
		if curN == 0:
			maxG = max(maxG, curVal)
			continue
		for idx, val in enumerate(arr[:curN]):
			ret.append([curN%(idx+1), curVal+val*(curN//(idx+1))])
	
	print(maxG)


if __name__ == "__main__":
	main()
