from algo1 import *
import myGraph as mg
import myLinkedList as mll

def createAdjacencyMatrix(Vertices,Edges):
	numOfVertices = mll.length(Vertices)
	matrix = createMatrixWithValue(numOfVertices,0)
	currentEdge = Edges.head
	while (currentEdge != None):
		valueOut = currentEdge.value[0]
		valueIn = currentEdge.value[1]
		matrix[getIndex(valueOut)][getIndex(valueIn)] = currentEdge.value[2]
		matrix[getIndex(valueIn)][getIndex(valueOut)] = currentEdge.value[2]
		currentEdge = currentEdge.nextNode
		
	return matrix


def createMatrixWithValue(size,value):
	matrix = Array(size,Array(size,value))
	for i in range(size):
		for j in range(size):
			matrix[i][j] = value
	return matrix

"""Crear Árbol abarcador de costo mínimo mediante PRIM"""
def PRIM(graph):
	edgeTree = mll.linkedList()
	numOfVertices = len(graph)
	visited = [0]
	while (len(visited) < numOfVertices):
		pos = getMinValue(graph,visited)
		if (pos[0] == None or pos[1] == None):
			break
			
		visited.append(pos[1])
		mll.add(edgeTree,(pos[0],pos[1]))
	verticesList = getListWithIndexes(numOfVertices)
	return mg.createGraph(verticesList,edgeTree)


"""Crear Árbol abarcador de costo mínimo mediante KRUSKAL"""
def KRUSKAL(graph):
	edgeTree = mll.linkedList()
	sets = mll.linkedList()
	numOfVertices = len(graph)
	verticesList = getListWithIndexes(numOfVertices)
	for index in range(numOfVertices):
		mll.add(sets,[index])
	edgesList = getSortedEdges(graph)
	
	currentEdge = edgesList.head
	while (currentEdge != None):
		vertexOut = getSet(sets,currentEdge.value[0])
		vertexIn = getSet(sets,currentEdge.value[1])
		if (vertexOut == vertexIn): 
			currentEdge = currentEdge.nextNode
			continue
			
		edge = currentEdge.value
		print(f"({edge[0]},{edge[1]}) = weight={edge[2]}")
		mll.add(edgeTree,[edge[0], edge[1], edge[2]])
		
		vertexOut.extend(vertexIn)
		mll.delete(sets,vertexIn)
		currentEdge = currentEdge.nextNode
	return mg.createGraph(verticesList,edgeTree)



"""Funciones auxiliares"""
def getSet(setList, value):
	currentNode = setList.head
	while (currentNode != None):
		currentSet = currentNode.value
		if (value in currentSet):
			return currentSet
		currentNode = currentNode.nextNode
	return None
	

def quickSortList(head,end):
	if (head == end) or (head.nextNode == end):
		return head
	pivot = head 
	curr = head.nextNode
	tail = pivot
	while (curr != end):
		currNext = curr.nextNode
		if (curr.value[2] < pivot.value[2]):
			curr.nextNode = head
			head = curr
		else:
			tail.nextNode = curr
			tail = curr
		curr = currNext
	tail.nextNode = end

	newHead = quickSortList(head,pivot)
	pivot.nextNode = quickSortList(pivot.nextNode,end)
	return newHead


def getEdges(graph):
	edgesList = mll.linkedList()
	numOfVertices = len(graph)
	for i in range(numOfVertices):
		for j in range(numOfVertices):
			if (graph[i][j] == 0):
				continue
			value = graph[i][j]
			if (mg.getNodeInList(edgesList,[i,j,value]) == None and
				 mg.getNodeInList(edgesList,[j,i,value]) == None):
				mll.add(edgesList,[i,j,graph[i][j]])
	return edgesList

	
def getSortedEdges(graph):
	edgesList = getEdges(graph)
	edgesList.head = quickSortList(edgesList.head,None)
	return edgesList

	
def getMinValue(graph, visitedVertices):
	minValue = 9999
	posX,posY = -1, -1
	for i in visitedVertices:
		for j in range(len(graph)):
			if (j not in visitedVertices and graph[i][j] != 0):
				if (minValue > graph[i][j]):
					minValue = graph[i][j]
					posX, posY = i, j
	print(f"({posX}, {posY}) = {minValue=}")
	return (None, None) if (posX == -1 or posY == -1) else (posX, posY)
	


def getListWithIndexes(numOfVertices):
	verticesList = mll.linkedList()
	for index in range(numOfVertices):
		mll.add(verticesList,numOfVertices - (index + 1))
	return verticesList
	

def printMatrix(matrix):
	for list in matrix:
		print(*list, sep = ", ")

def getIndex(value):
    return value - 1