def sol(n):
	if n <= 1:
		return 1

	ret = 0
	for num in [2, 1]:
		ret += sol(n-num)

	return ret

#	def factorial(n):
#		ret = 1
#		for i in range(1, n+1):
#			ret *= i
#		return ret
#	
#	def sol2(n):
#		ret = 0
#		max_zeros	= n // 2
#		for zeros in range(max_zeros):
#			ones	= n - 2*zeros
#			ret += factorial(ones + zeros - 1) / factorial(zeros) / factorial(ones - 1)
#		return ret

n = int(input())
print(sol(n)%15746)
