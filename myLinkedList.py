"""nombre: Julián Vidal
Ejercitación TAD LinkedList"""
class linkedList:
	head = None

class Node:
	value = None
	nextNode = None

	def __init__(self,value):
		self.value = value
		

"""Add"""
def add(LL,element):
	nodeToAdd = Node(element)
	nodeToAdd.nextNode = LL.head
	LL.head = nodeToAdd
#Complejidad constante en lista, tad no utilizado en array

"""Lenght"""
def length(LL):
	size = 0
	currentNode = LL.head
	while (currentNode != None):
		currentNode = currentNode.nextNode
		size += 1

	return size

#Complejidad lineal en lista, constante en array


"""Search"""
def search(LL,element):
	currentNode = LL.head
	
	if (currentNode == None):
		return None

	index = 0
	size = length(LL)
	for i in range(size):
		if (currentNode.value == element):
			return index

		currentNode = currentNode.nextNode
		index += 1
	return None

#Complejidad lineal, tanto en lista como en array


"""Insert"""
def insert(LL,element,index):
	if (index == 0):
		add(LL,element)
		return 0

	prevNode = getNode(LL,index - 1)
	if (prevNode == None):
		return None

	nodeToInsert = Node(element)
	nodeToInsert.nextNode = prevNode.nextNode
	prevNode.nextNode = nodeToInsert
	
	return index
#Complejidad lineal, tanto en lista como en array


"""Delete"""
def delete(LL,element):
	index = search(LL,element)
	return delete_by_pos(LL,index)


def delete_by_pos(LL,index):
	if (index == None):
		return None
	if (index == 0):
		LL.head = LL.head.nextNode
		return 0

	prevNode = getNode(LL,index - 1)
	prevNode.nextNode = prevNode.nextNode.nextNode
	return index
#Complejidad lineal, tanto en lista como en array

"""Access"""
def access(LL,index):
	currentNode = getNode(LL,index - 1)
	if (currentNode == None or currentNode.nextNode == None):
		return None

	return currentNode.nextNode.value
	
#Complejidad lineal en lista, constante en array


"""Update"""
def update(LL,element,index):
	currentNode = getNode(LL,index)
	if (currentNode == None):
		return None

	currentNode.value = element
	return index
#Complejidad lineal en lista, tad no implementado en array


"""Dequeue"""
def dequeue(LL):
	leng = length(LL)
	if (leng == 1):
		currentNode = LL.head
		LL.head = None
	else:
		prevNode = getNode(LL,leng - 2)
		currentNode = prevNode.nextNode
		prevNode.nextNode = None
	return currentNode.value


"""POP"""
def pop(LL):
	if (LL.head == None):
		return None
	currentNode = LL.head
	LL.head = LL.head.nextNode
	return currentNode.value

"""Auxiliares"""
def getNode(LL,index):
	currentNode = LL.head
	currentIndex = 0

	while (currentNode != None):
		if (currentIndex == index):
			return currentNode
		currentNode = currentNode.nextNode
		currentIndex += 1

	return None

def getIndex(LL,node):
	index = 0
	currentNode = LL.head
	
	while (currentNode != None):
		if (currentNode == node):
			return index
		index += 1
		currentNode = currentNode.nextNode

	return 0


def reverse(LL):
	prevNode = None 
	currentNode = LL.head 
	nextNode = currentNode.nextNode 
	while (currentNode != None):
		currentNode.nextNode = prevNode
		prevNode = currentNode
		currentNode = nextNode
		if (nextNode != None):
			nextNode = nextNode.nextNode

	LL.head = prevNode


def printList(LL):
	currentNode = LL.head
	print("[", end="")
	while (currentNode != None):
		print(currentNode.value, end="")
		if (currentNode.nextNode != None):
			print("",end=", ")
		currentNode = currentNode.nextNode
	print("]")