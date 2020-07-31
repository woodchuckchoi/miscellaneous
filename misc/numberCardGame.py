'''
Recursive, Memoization
'''

def sol(n, k, used=set(), memo=dict(), done=[]):
	if k == 0:
		return 0
	if k == 1:
		closest = n
		so_far = sum(used)
		while closest <= so_far:
			closest += closest
		diff = closest - so_far

		if diff < n and diff not in used:
			used.add(diff)
			if used in done:
				return 0
			done.append(used)
			print(done)
			return 1
		return 0

	if (n, k, tuple(used)) in memo:
		return memo[(n, k, tuple(used))]

	ret = 0
	for num in [x for x in range(n) if x not in used]:
		used_copy = used.copy()
		used_copy.add(num)
		ret += sol(n, k - 1, used_copy, memo, done)
	memo[(n, k, tuple(used))] = ret

	return ret

print(sol(7, 4))
