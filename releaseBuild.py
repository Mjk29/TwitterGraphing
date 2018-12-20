
class graph:
	def __init__(self):
		self.nodeList = {}
		self.counter = 0
	def printGraph(self):
		print("┌──────────┬──────────┬──────────┬──────────┬──────────┐")
		for key in self.nodeList:
			self.nodeList[key].printNode()
	def printPath(self, node, limitCounter):
		limitCounter+=1
		if self.nodeList[node].parent == -1:
			return node
		returnString = self.printPath(self.nodeList[node].parent, limitCounter)
		returnString+= " " + str(node)
		return returnString
	def clear(self):
		for node in self.nodeList:
			self.nodeList[node].parent = -1
			self.nodeList[node].preV = -1
			self.nodeList[node].postV = -1
			self.nodeList[node].depth = 0




class node:
	def __init__(self):
		self.name = "asd"
		self.edgeList = []
		self.preV = -1
		self.postV = -1
		self.parent = -1
		self.depth = 0
	def printNode(self):

		print("│   name   │   preV   │   postV  │  parent  │  depth   │")
		printString = "│   "+self.name
		for x in range(7-len(self.name)):
			printString+=" "

		printString+="│   "+str(self.preV)
		for x in range(7-len(str(self.preV))):
			printString+=" "

		printString+="│   "+str(self.postV)
		for x in range(7-len(str(self.postV))):
			printString+=" "

		printString+="│   "+str(self.parent)
		for x in range(7-len(str(self.parent))):
			printString+=" "


		printString+="│   "+str(self.depth)
		for x in range(7-len(str(self.depth))):
			printString+=" "
		printString+="│ "

		print(printString)
		print("├──────────┼──────────┼──────────┼──────────┼──────────┤")

completed = {}
counter = 0
scCount = 0
scArr = [[]]


def project(functionType, startNode, endNode, maxDepth):
	# Pick file to operate on
	# combinedFile = open("letterTest", "r")
	# combinedFile = open("testEdges.edges", "r")
	combinedFile = open("twitter_combined.txt", "r")
	# combinedFile = open("twitterHalf", "r")
	# combinedFile = open("smalltest2.txt", "r")
	
	# Create edge list 
	edgeList = []
	lineCount = 0
	for line in combinedFile:
		# if lineCount > 1000:
		# 	break
		edgeList.append((line.strip()).split())
		lineCount+=1
	combinedFile.close() 

	# Init graphs
	twitterGraph = graph()

	# Creates the graph from 0 to 1
	createGraph(edgeList, 0, 1, twitterGraph, "Creating-Initial-Graph ")
	print("\n")

	if functionType == "scc":
		stronglyConnected(twitterGraph, edgeList)
	if functionType == "rec":
		if str(startNode) in twitterGraph.nodeList and str(endNode) in twitterGraph.nodeList:
			# startNode = "11348282"
			# endNode =  "34743251"
			recomendation(str(startNode), str(endNode), maxDepth, twitterGraph)

			# for start in range(1,10):
			# 	for end in range(1,10):
			# 		# maxDepth = x
			# 		print("Start Node : " + str(start) + " End Node : " + str(end))
			# 		recomendation(str(start), str(end), 4, twitterGraph)
			# 		twitterGraph.clear()
		else:
			print("Nodes not in graph")
			return


	# sort alphebetically for test
	# for alNode in reverseGraph.nodeList:
	# 	reverseGraph.nodeList[alNode].edgeList = sorted(reverseGraph.nodeList[alNode].edgeList)
	# global scCount
	# global scArr

	# for startNode in descPostV:
	# 	if reverseGraph.nodeList[startNode].postV == -1:
	# 		scArr.append([])
	# 		scCount += 1
	# 		scArr[scCount]=[]
	# DFSSearch5(reverseGraph, descPostV)
	# reverseGraph.printGraph()

	# # Removes empty first element from array
	# # First element used for formatting, not needed when done
	# scArr.pop(0)

	# scArr.sort(key=len, reverse = True)
	# print(scArr)
	# # for conn in scArr:
	# # 	if len(conn) > 1:
	# # 		print(len(conn))




def recomendation(startNode, endNode, maxDepth, graph):
	returnedPaths = DFSSearch7_2(graph, startNode, endNode, maxDepth)
	import datetime
	writeFileName = "REC"+datetime.datetime.now().strftime("%Y-%m-%d %H_%M")
	writeFile = open(writeFileName, "w+")
	if  returnedPaths == None:
		print("No Paths to Target")
		writeFile.close()
		return
	succ = 0
	
	if maxDepth == 0:
		for path in returnedPaths:
			succ = 1
			writeFile.write("\n"+str(len(path)-1)+" : "+str(path))
	else:
		for path in returnedPaths:
			if len(path)-1 == maxDepth:
				succ = 1
				writeFile.write("\n"+str(len(path)-1)+" : "+str(path))
	if succ == 0:
		writeFile.write("No paths of correct length")


		# print("Graph nodes : " + graphSize)
		# for strongC in stronglyConnectedList:
		# 	if len(strongC) > 50:
		# 		writeFile.write("\nLength of Strongly Connected : "+ str(len(strongC)) + "\n")
		# 		writeFile.write(str(strongC))
		# 		print("\nLength of Strongly Connected : "+ str(len(strongC)))
				
		writeFile.close()

	# print("")
	# if  returnedPaths == None:
	# 	print("No Paths to Target")
	# 	return
	# succ = 0
	
	# if maxDepth == 0:
	# 	for path in returnedPaths:
	# 		succ = 1
	# 		print(" "+str(len(path)-1)+" : "+str(path))
	# else:
	# 	for path in returnedPaths:
	# 		if len(path)-1 == maxDepth:
	# 			succ = 1
	# 			print(" "+str(len(path)-1)+" : "+str(path))
	# if succ == 0:
	# 	print("No paths of correct length")
	

def DFSSearch7_2(graphName, startNode, endNode, maxDepth):
	if startNode == endNode:
		print("start and end same")
		print("")
		return

	widgets=[
	    ' [', progressbar.DynamicMessage("Finding_all_paths"), '] ',
	    ' [', progressbar.Timer(), '] ',
	    ' [', progressbar.BouncingBar(marker='#', left='|', right='|', fill='-', fill_left=True), '] ',
    progressbar.Bar(),]
	bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength,widgets=widgets)
	barCounter =0


	counter = 0
	breaker = 0
	scCount = 0
	barCounter = 0
	pathCounter = 0

	completed = set()
	visited  = set()
	allPaths = []

	parentNode = collections.deque()
	currentPath = collections.deque()
	lastAdded = collections.deque()
	checkLast = collections.deque()




	scList = []	
	scList.append([])


	visited.add(startNode)
	# currentPath.appendleft(startNode)
	currentPath.appendleft(0)
	 # Set children to current path node
	for edge in graphName.nodeList[startNode].edgeList:
		graphName.nodeList[edge].parent = startNode
		graphName.nodeList[edge].depth = 1
		if edge == endNode:
			graphName.nodeList[edge].parent = startNode
			graphName.nodeList[edge].depth = 1
			allPaths.append(graphName.printPath(edge, 0).split())

		else:
			currentPath.appendleft(edge)

	depth = 1
	tmpNode = startNode
	parentNode.appendleft(startNode)	
	lastAdded.appendleft(startNode)
	loopCounter = 0
	maxCount = 10000


	while len(currentPath) > 0:
		barCounter +=1
		bar.update(barCounter)


		loopCounter +=1
		if loopCounter > maxCount:
			break

		if currentPath[0] == 0:
			parentNode.popleft()
			currentPath.popleft()
			continue
	
		currentNode = currentPath.popleft()
		for node in lastAdded:
			checkLast.append(node)
		lastAdded.clear()


		parentNode.appendleft(currentNode)	
		currentPath.appendleft(0)
		depth +=1
		for edge in graphName.nodeList[currentNode].edgeList:
			# If edge already checked skip
			if edge == endNode:
				graphName.nodeList[edge].parent = currentNode
				graphName.nodeList[edge].depth = graphName.nodeList[currentNode].depth+1
				allPaths.append(graphName.printPath(edge, 0).split())
				continue
			if edge in checkLast:
				continue
			
			if maxDepth == 0:
				if graphName.nodeList[edge].parent == -1:
					graphName.nodeList[edge].depth = graphName.nodeList[currentNode].depth+1
					graphName.nodeList[edge].parent = currentNode
				currentPath.appendleft(edge)
				lastAdded.appendleft(edge)

			elif depth < maxDepth:
				if graphName.nodeList[edge].parent == -1:
					graphName.nodeList[edge].depth = graphName.nodeList[currentNode].depth+1
					graphName.nodeList[edge].parent = currentNode				
				currentPath.appendleft(edge)
				lastAdded.appendleft(edge)

	# Cleanup if last element in scList is empty
	if len(scList[len(scList)-1]) == 0:
		del scList[len(scList)-1]
	# graphName.printGraph()
	return allPaths



def stronglyConnected(twitterGraph, edgeList):
	
	reverseGraph = graph()

	firstOrder = []
	for x in twitterGraph.nodeList:
		firstOrder.append(x)
	graphSize = str(len(firstOrder))
	
	DFSSearch5(twitterGraph, firstOrder, "First-DFS              ")
	print("\n")

	descPostV = getPostOrder(twitterGraph)

	# Reverse all edges
	completed.clear()
	counter = 0

	createGraph(edgeList, 1,0, reverseGraph, "Creating-Reversed-Graph")
	print("\n")

	stronglyConnectedList = []
	stronglyConnectedList = DFSSearch5(reverseGraph, descPostV, "Second-DFS             ")
	print("\n")

	import datetime
	writeFileName = "SCC_"+datetime.datetime.now().strftime("%Y-%m-%d %H_%M")

	writeFile = open(writeFileName, "w")
	print("Graph nodes : " + graphSize)
	for strongC in stronglyConnectedList:
		if len(strongC) > 50:
			writeFile.write("\nLength of Strongly Connected : "+ str(len(strongC)) + "\n")
			writeFile.write(str(strongC))
			print("\nLength of Strongly Connected : "+ str(len(strongC)))
			
	writeFile.close()









def createGraph(edgeList, sNode, fNode, graphName, barName):
	widgets=[
    ' [', progressbar.DynamicMessage(barName), '] ',
    ' [', progressbar.Timer(), '] ',
    ' [', progressbar.BouncingBar(marker='#', left='|', right='|', fill='-', fill_left=True), '] ',
    progressbar.Bar(),]
	bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength,widgets=widgets)
	barCounter =0
	# Creates the graph in o(n)
	for edge in edgeList:
		barCounter +=1
		bar.update(barCounter)
		# Setup the completed list
		if edge[sNode] not in completed:
			completed[edge[sNode]] = 0
		if edge[fNode] not in completed:
			completed[edge[fNode]] = 0

		# Setup the graph nodes
		if edge[sNode] not in graphName.nodeList:
			tempNode = node()
			tempNode.name = edge[sNode]
			tempNode.edgeList.append(edge[fNode])
			graphName.nodeList[edge[sNode]] = tempNode
		else:
			graphName.nodeList[edge[sNode]].edgeList.append(edge[fNode])
		if edge[fNode] not in graphName.nodeList:
			tempNode = node()
			tempNode.name = edge[fNode]
			graphName.nodeList[edge[fNode]] = tempNode




# Gets the post order 
def getPostOrder(twitterGraph):
	nodePost = []
	for node in twitterGraph.nodeList:
		nodePost.append([node,twitterGraph.nodeList[node].postV])
	nodePost.sort(key=lambda x: x[1], reverse=True)
	nodeList = []
	for pair in nodePost:
		nodeList.append(pair[0])
	return nodeList





def DFSSearch5(graphName, nameArr, barName):
	counter = 0
	completed = set()
	breaker = 0
	visited  = set()
	scList = []	
	scList.append([])
	import collections 
	currentPath = collections.deque()
	scCount = 0
	barCounter = 0
	widgets=[
    ' [', progressbar.DynamicMessage(barName), '] ',
    ' [', progressbar.Timer(), '] ',
    ' [', progressbar.BouncingBar(marker='#', left='|', right='|', fill='-', fill_left=True), '] ',
    progressbar.Bar(),
	]
	bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength,widgets=widgets)

	# # Check all initial nodes
	for currentNode in nameArr:
		if len(scList[scCount]) != 0:
			scCount +=1
	 	# Check if node already visited
		if currentNode in completed:
			continue
		else:
			visited.add(currentNode)
			currentPath.appendleft(currentNode)
			graphName.nodeList[currentNode].preV = counter
			counter +=1 
	 	# Set children to current path node
		for edge in graphName.nodeList[currentNode].edgeList:
	 		# Check if edge already visited
			if edge in completed:
				continue
			else:
				currentPath.appendleft(edge)
		while len(currentPath) > 0:
			barCounter +=1
			bar.update(barCounter)
			if len(scList) == scCount+1:
				scList.append([])
			tmpNode = currentPath.popleft()
			if tmpNode in completed:
				continue
			else:
				if tmpNode in visited:
					scList[scCount].append(tmpNode)
					graphName.nodeList[tmpNode].postV = counter
					counter +=1
					completed.add(tmpNode)
					continue
				else:
					graphName.nodeList[tmpNode].preV = counter
					counter +=1
					visited.add(tmpNode)
				# if there are no children, this is a leaf and can be post set
				if len(graphName.nodeList[tmpNode].edgeList) == 0:
					graphName.nodeList[tmpNode].postV = counter
					counter += 1
					completed.add(tmpNode)
					continue
				else:
					currentPath.appendleft(tmpNode)
					for subNode in graphName.nodeList[tmpNode].edgeList:
						if subNode not in visited:
							currentPath.appendleft(subNode)	
	# Cleanup if last element in scList is empty
	if len(scList[len(scList)-1]) == 0:
		del scList[len(scList)-1]

	return scList
	



if __name__ == '__main__':
	import timeit
	import sys
	import time
	import progressbar
	import collections 

	sortBar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
	barUpdateCount = 0

	sys.setrecursionlimit(1500)
	print("running")

	if sys.argv[1] == "scc":
		overallTime = timeit.repeat("project(\"scc\",0,0,0)", setup="from __main__ import project", repeat=1, number=1)
	elif sys.argv[1] == "rec":
		if len(sys.argv) == 5:
			overallTime = timeit.repeat("project(\"rec\","+sys.argv[2]+","+sys.argv[3]+","+sys.argv[4]+")", setup="from __main__ import project", repeat=1, number=1)
		else:
			print("requires start & end nodes and MaxDepth")
			quit()

	else:
		print("bad arguments")
		quit()

	# overallTime = timeit.repeat("project(\"scc\")", setup="from __main__ import project", repeat=1, number=1)
	# overallTime = timeit.repeat("project(\"rec\")", setup="from __main__ import project", repeat=1, number=1)
	# overallTime = timeit.repeat("project(\""+str(sys.argv[1])+"\")", setup="from __main__ import project", repeat=1, number=1)


	print("Total RunTime : "+str(overallTime))
	print('\n')
