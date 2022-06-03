from algo1 import *
import myLinkedList as mll

class Node(): #Reemplazo al node de linkedList
	value = None
	color = "White"
	nextNode = None

	def __init__(self,value):
		self.value = value


"""Crear un grafo"""
def addListNode(LL,value):
	newNode = Node(value)
	newNode.nextNode = LL.head.nextNode
	LL.head.nextNode = newNode


def addConnection(graph,vertexIn,vertexOut):
	list = getListWithValue(graph,vertexIn)
	addListNode(list,vertexOut)

	
def createGraph(Vertices, Edges):
	numOfVertices = mll.length(Vertices)
	newGraph = Array(numOfVertices,mll.linkedList())
	currentVertex = Vertices.head
	for currentIndex in range(numOfVertices):
		newGraph[currentIndex] = mll.linkedList()
		newGraph[currentIndex].head = Node(currentVertex.value)
		currentVertex = currentVertex.nextNode

	currentEdge = Edges.head
	numOfEdges = mll.length(Edges)
	for currentIndex in range(numOfEdges):
		vertexIn = currentEdge.value[0]
		vertexOut = currentEdge.value[1]
		addConnection(newGraph,vertexIn,vertexOut)
		addConnection(newGraph,vertexOut,vertexIn) #Si comentamos esta línea se vuelve un grafo dirigido
		currentEdge = currentEdge.nextNode
	return newGraph


"""Comprobar si existe un camino entre dos vertices"""		
def existPath(graph,start,end):
	return getPath(graph,mll.linkedList(),start,None,end)

"""Ver si un grafo es conexo"""
def isConnected(graph):
	return countConnections(graph) == 1;


"""Comprobar si el grafo es un árbol"""
def isTree(graph):
	if (not isConnected(graph)):
		return False
	numOfVertices = len(graph)
	numOfEdges = getNumberOfEdges(graph)
	return (numOfEdges//2 == numOfVertices - 1)


"""Comprobar si un grafo es completo"""
def isComplete(graph):
	numOfVertices = len(graph)
	for list in graph:
		if (mll.length(list) != numOfVertices):
			return False
	return True


"""Convertir un grafo a árbol"""
def convertTree(graph):
	edgesToDelete = mll.linkedList()
	if (not isConnected(graph)):
		return edgesToDelete
	edgesInOriginal = getEdgesList(graph)
	visitDfsTree = convertToDFSTree(graph,graph[0].head.value)
	edgesInDfs = getEdgesList(visitDfsTree)

	currentOriginal = edgesInOriginal.head
	while (currentOriginal != None):
		if (mll.search(edgesInDfs,currentOriginal.value) == None):
			mll.add(edgesToDelete,currentOriginal.value)
		currentOriginal = currentOriginal.nextNode
	
	return edgesToDelete
			

"""Contar la cantidad de componentes conexas del grafo"""
def visitDfs(graph,visited,value):
	currentVertex = getHeadWithValue(graph,value)
	while (currentVertex != None):
		if (currentVertex.value not in visited):
			visited.append(currentVertex.value)
			visitDfs(graph,visited,currentVertex.value)
		currentVertex = currentVertex.nextNode

	
def countConnections(graph):
	visited = []
	components = 0
	for list in graph:
		if (list.head.value in visited):
			continue
		visited.append(list.head.value)
		components += 1
		visitDfs(graph, visited, list.head.value)
	return components

	
"""BreathFirstSearch, búsqueda en anchura"""
def BreadthFirstSearch(graph, edges, root):
	currentList = getListWithValue(graph,root)
	currentVertex = currentList.head
	visitedValues = []
	visitedValues.append(currentVertex.value)
	auxQueue = mll.linkedList()
	mll.add(auxQueue,currentVertex.value)
	while (auxQueue.head != None):
		currentValue  = mll.dequeue(auxQueue)
		currentVertex = getHeadWithValue(graph,currentValue).nextNode
		while (currentVertex != None):
			if (currentVertex.value not in visitedValues):
				mll.add(edges, (currentValue,currentVertex.value))
				visitedValues.append(currentVertex.value)
				mll.add(auxQueue,currentVertex.value)
			currentVertex = currentVertex.nextNode
	
		

def convertToBFSTree(graph,root):
	resetColors(graph)
	if (not isConnected(graph)):
		return []
	if (getListWithValue(graph,root) == None):
		return []
	vertices = getVerticesList(graph)
	edges = mll.linkedList()
	BreadthFirstSearch(graph, edges, root)
	return createGraph(vertices, edges)


"""DepthFirstSearch, búsqueda en profundidad"""
def DepthFirstSearch(graph, edges, root):
	currentList = getListWithValue(graph,root)
	numOfEdges = mll.length(currentList)
	currentVertex = currentList.head
	currentVertex.color = "Gray"
	for index in range(numOfEdges):
		if (getHeadWithValue(graph,currentVertex.value).color == "White"):
			mll.add(edges,(root, currentVertex.value))
			DepthFirstSearch(graph,edges,currentVertex.value)
		currentVertex = currentVertex.nextNode
	currentList.head.color = "Black"

	
def convertToDFSTree(graph, root):
	resetColors(graph)
	if (not isConnected(graph)):
		return []
	if (getListWithValue(graph,root) == None):
		return []

	vertices = getVerticesList(graph)
	edges = mll.linkedList()
	DepthFirstSearch(graph,edges,root)
	return createGraph(vertices, edges)


"""Encontrar el camino más corto entre dos vertices"""
def bestRoad(graph,start,end):
	listWithStart = getListWithValue(graph,start)
	listWithEnd = getListWithValue(graph,end)
	if (listWithStart == None or listWithEnd == None):
		return None
	bfsGraph = convertToBFSTree(graph,getHeadWithValue(graph,start))
	path = mll.linkedList()
	if (getPath(graph,path,start,None,end)):
		mll.reverse(path)
		return path
	return mll.linkedList()


"""Comprobar si un grafo es bipartito"""
def isBipartite(graph):
	visitedVertices = createListWithValue(len(graph), False)
	levels = createListWithValue(len(graph), 0)
	auxList = mll.linkedList()
	visitedVertices[0] = True
	levels[0] = 0
	mll.add(auxList,graph[0].head.value)

	while (mll.length(auxList) > 0):
		currentValue = mll.dequeue(auxList)
		currentList = getListWithValue(graph,currentValue)
		currentVertex = currentList.head
		while (currentVertex.nextNode != None):
			currentVertex = currentVertex.nextNode
			index = getIndex(graph,currentVertex.value)
			if (not visitedVertices[index]):
				visitedVertices[index] = True
				levels[index] = levels[getIndex(graph,currentValue)]+ 1
				mll.add(auxList,currentVertex.value)

			elif (levels[index] == levels[getIndex(graph,currentValue)]):
				return False
	return True
			

"""Funciones Auxiliares"""	
def createListWithValue(size,value):
	list = Array(size,value)
	for i in range(size):
		list[i] = value
	return list
			

def getPath(graph,path,start,prev, end):
	currentList = getListWithValue(graph,start)
	if (getNodeInList(currentList, end) != None):
		mll.add(path,(start,end))
		return True
		
	currentVertex = currentList.head.nextNode
	while (currentVertex != None):
		if (getNodeInList(path,(start,currentVertex.value)) == None 
			 and getNodeInList(path,(currentVertex.value,start)) == None):
				mll.add(path,(start,currentVertex.value))
				if (getPath(graph,path,currentVertex.value,start,end) == True):
					return True
		currentVertex = currentVertex.nextNode
	return (path.head.value[1] == end)


def resetColors(graph):
	for list in graph:
		list.head.color = "White"
		
	
def getNumberOfEdges(graph):
	numOfVertices = len(graph)
	numOfEdges= 0
	for currentIndex in range(numOfVertices):
		currentVertex = graph[currentIndex].head.nextNode
		while (currentVertex != None):
			numOfEdges += 1
			currentVertex = currentVertex.nextNode
	return numOfEdges


def printGraph(graph):
	for list in graph:
		mll.printList(list)


def getNodeInList(LL,value):
	currentNode = LL.head
	while (currentNode != None):
		if (currentNode.value == value):
			return currentNode
		currentNode = currentNode.nextNode
	return None


def getListWithValue(graph,value):
	for list in graph:
		if (list.head.value == value):
			return list
	return None


def getIndex(graph,value):
	for currentIndex in range(len(graph)):
		if (graph[currentIndex].head.value == value):
			return currentIndex
	return None

	
def getHeadWithValue(graph,value):
	list = getListWithValue(graph,value)
	if (list != None):
		return list.head
	return None

	
def getVerticesList(graph):
	verticesList = mll.linkedList()
	for list in graph:
		mll.add(verticesList,list.head.value)
	mll.reverse(verticesList)
	return verticesList


def getEdgesList(graph):
	edgesList = mll.linkedList()
	for list in graph:
		currentValue = list.head.value
		currentEdge = list.head.nextNode
		while (currentEdge != None):
			mll.add(edgesList,(currentValue, currentEdge.value))
			currentEdge = currentEdge.nextNode
	return edgesList
