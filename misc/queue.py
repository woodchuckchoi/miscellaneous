queue = []
ret = []
def main():
	n = int(input())
	for _ in range(n):
		order = input()
		if order == "pop":
			try: ret.append(queue.pop(0))
			except: ret.append(-1)
		elif order[:4] == "push":
			queue.append(int(order.split()[1]))
		elif order == "size":
			ret.append(len(queue))
		elif order == "empty":
			ret.append(int(len(queue)==0))
		elif order == "front" or order == "back":
			try: 
				if order == "front":
					ret.append(queue[0])
				else:
					ret.append(queue[-1])
			except: ret.append(-1)

	for i in ret:
		print(i)
if __name__ == "__main__":
	main()
