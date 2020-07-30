class Tree:
	left	= None
	right	= None 
	
	def __init__(self, val):
		self.val = val

	def set_leaf(self, t):
		if t.val <= self.val and self.left == None: self.left = t
		elif t.val > self.val and self.right == None: self.right = t
		else: raise Exception('Invalid Action!')

	def show_val(self):
		return self.val

	def show_tree(self):
		if self.left != None: print("{}/{}".format(' '*len(str(self.val)), self.left.val))
		print("{}".format(self.val))
		if self.right != None: print("{}\\{}".format(' '*len(str(self.val)), self.right.val))

def main():
	a = Tree(5)
	a.set_leaf(Tree(4))
	a.set_leaf(Tree(92))
	a.show_tree()

if __name__ == "__main__":
	main()
