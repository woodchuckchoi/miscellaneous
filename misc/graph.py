import random

class Graph:
	def __init__(self, val):
		self.val	= val
		self.nodes	= []
	def __str__(self):
		return "Node value: {}, Connected nodes: [{}]".format(self.val, self.nodes)
	def __name__(self):
		return self.__str__()
	def __repr__(self):
		return "Node value: {}".format(self.val)
	def add_node(self, node):
		self.nodes.append(node)


def walk(node, trace):
	if set(node.nodes).intersection(trace) == set(node.nodes):
		return

	trace.append(node)

	for n in [x for x in node.nodes if x not in trace]:
		walk(n, trace)

	return trace

def main():
	nodes = []
	for i in range(20):
		nodes.append(Graph(random.randint(1, 100)))

	for i in range(len(nodes)):
		for j in nodes[:i] + nodes[i+1:]:
			if random.choice([True, False]): nodes[i].add_node(j)
	print(walk(nodes[0], []))

if __name__=="__main__":
	main()
