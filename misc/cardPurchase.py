<<<<<<< HEAD
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
=======
n = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = price[1]
dp[2] = max(price[2], 2*price[1])

for i in range(3, n+1):
	dp[i] = price[i]
	for j in range(1, i//2 + 1):
		dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])
>>>>>>> e57099e04d2931be7c4f7c1af1085c5aef0587c4
