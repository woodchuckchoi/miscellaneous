def main():
	minBurger	= 2000
	minDrink	= 2000
	for i in range(5):
		price	= int(input())
		if i <= 2:
			minBurger	= min(minBurger, price)
		else:
			minDrink	= min(minDrink, price)
	print(minBurger + minDrink - 50)


if __name__ == "__main__":
	main()
