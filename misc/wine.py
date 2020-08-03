n   = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
memo = dict()

idx     = n-1

while idx >= 0:
    
    for step in [1, 2, 3]:
        
        if idx + step >= n:
            if (idx, False) not in memo:
                memo[(idx, False)] = arr[idx]
            else: 
                memo[(idx, False)] = max(arr[idx], memo[(idx, False)])
            break
        
        if step == 1:
            if (idx + step, False) in memo:
                memo[(idx, True)] = memo[(idx+step, False)] + arr[idx]
        else:
            next_true   = memo[(idx+step, True)] if (idx+step, True) in memo else 0
            next_false  = memo[(idx+step, False)] if (idx+step, False) in memo else 0
            memo[(idx, False)] = max(max(next_false, next_true) + arr[idx], memo[(idx, False)] if (idx, False) in memo else 0)

    idx -= 1

true_val = memo[(0, True)] if (0, True) in memo else 0
false_val = memo[(0, False)] if (0, False) in memo else 0
print(max(true_val, false_val))
