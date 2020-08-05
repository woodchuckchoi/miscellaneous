def main():
	n = int(input())
	arr = [1,1,1,2,2]
	ret = []
	for i in range(n):
		num = int(input())
		if num <= len(arr):
			ret.append(arr[num-1])
			continue
		for j in range(len(arr), num):
			arr.append(arr[-5] + arr[-1])
		ret.append(arr[-1])
	for i in ret:
		print(i)
	print(arr)
if __name__ == "__main__":
	main()
