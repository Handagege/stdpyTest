#!/usr/bin/python


class Node():
	
	def __init__(self,data):
		self.__data = data
		self.__left = None
		self.__right = None


	def setLeftBranch(self,node):
		self.__left = node


	def setRightBranch(self,node):
		self.__right = node

	
	def getData(self):
		return self.__data

	
	def getLeftBranch(self):
		return self.__left

	
	def getRightBranch(self):
		return self.__right


class BinaryTree():
	
	def __init__(self,root=Node("root")):
		self.__root = root
	

	def setRoot(self,root):
		self.__root = root


	def getRoot(self):
		return self.__root


def inOrder(node):
	if not node:
		return
	print node.getData()
	left = node.getLeftBranch()
	right = node.getRightBranch()
	inOrder(left)
	inOrder(right)


def hierarchyTraverse(node,queue):
	if node:
		queue.insert(0,node)
	while queue:
		tnode = queue.pop()
		print tnode.getData()
		left = tnode.getLeftBranch()
		right = tnode.getRightBranch()
		if left:
			queue.insert(0,left)
		if right:
			queue.insert(0,right)
		
	
node = Node("zhanghanR")
l1 = Node("llllleft")
r1 = Node("rrrrright")
node.setLeftBranch(l1)
l1.setLeftBranch(Node("iaml2"))
l1.setRightBranch(Node("iamr2"))
r1.setLeftBranch(Node("iam33333"))
node.setRightBranch(r1)
t = BinaryTree(node)

def test1():
	inOrder(t.getRoot())
	
	
def test2():
	queue = []
	hierarchyTraverse(t.getRoot(),queue)
	


if __name__ == '__main__':
	test2()
	


