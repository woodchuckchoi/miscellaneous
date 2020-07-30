def quickSort(arr):
	if len(arr) <= 1:
		return arr
	left, right = [], []
	for i in arr[:-1]:
		if i <= arr[-1]: left.append(i)
		else: right.append(i)
	left	= quickSort(left)
	right	= quickSort(right)
	return left + [arr[-1]] + right

def main():
	arr = [1,5,4,32,4,6,7,8,4,22,2,2,5,56,7,5,433,3,6,4,3,34]
	print(quickSort(arr))

if __name__ == "__main__":
	main()
