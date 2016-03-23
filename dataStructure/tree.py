#!/usr/bin/python


class node:
	
	def __init__(self,data):
		self.__data = data
		self.__children = []


	def getData(self):
		return self.__data
	

	def getChildren(self):
		return self.__children
	

	def add(self,node):
		self.__children.append(node)


class tree:
	
	def __init__(self,root=node("root")):
		self.__root = root


	def getRoot(self):
		return self.__root


	def insert(self,path,node):
		pass

	
	def delete(self,path):
		pass

	
	def search(self,path):
		pass


	def inOrder(self,node):
		result = [node.getData()]
		for child in node.getChildren():
			result.extend(self.inOrder(child))
		return result


if __name__ == '__main__':
	a = node(1)
	b = node(2)
	c = node(3)
	d = node(4)
	e = node(5)
	f = node(6)
	g = node(7)
	h = node(8)
	i = node(9)
	j = node(10)
	k = node(11)

	i.add(a)
	i.add(g)
	e.add(j)
	e.add(c)
	h.add(i)
	h.add(e)
	d.add(f)
	b.add(h)
	b.add(d)

	myTree = tree(b)
	print myTree.inOrder(myTree.getRoot())
	i.add(k)
	print myTree.inOrder(myTree.getRoot())

		

