# Try One at Neural Net for pattern recognition (c) Alex Shukhman, 2016
from math import *
from random import *

class Node:
    def __init__(self, name, inputnodes, iweight, function, outputNumber):
        self.inputs = inputnodes
        self.iw = iweight # from upstream nodes
        self.name = name
        self.function = function
        self.setOWeights(outputNumber)
    def setOWeights(self, outputNumber):
        self.oWeights = {}
        for i in range(outputNumber):
            self.oWeights[i] = random()
    def findStartNode(self, node, previousNode=None):
        if node.findStartNode(node, previousNode) == None:
            if previousNode != None:
                return previousNode.inputs
            else:
                print ('started too far back')
                return 
        else:
            for i in self.inputs:
                return i.findStartNode(i,self)
    def runSim(self,oweight):
        minilist = []
        for i in range(len(self.inputs)):
            minilist.append(self.inputs[i].runsim(self.iw[i]))
        self.fx = classmethod(self.function(self,minilist))
        return oweight*self.fx(minilist)

class InputNode(Node):
    def __init__(self, name, value, outputNumber):
        self.function = None
        self.iw = None
        self.inputs = {}
        self.value = value
        self.setOWeights(outputNumber)
        
    def setOWeights(self, outputNumber):
        self.oWeights = {}
        for i in range(outputNumber):
            self.oWeights[i] = random()
            
    def findStartNode(self,node,previousNode=None):
        return None
    def runSim(self,oweight):
        return self.value*oweight
    
class OutputNode(Node):
    def __init__(self, name, value, inputnodes, iweights):
        self.inputs = inputnodes
        self.iws = iweights
        self.value = value
        self.function = None
    def findError(self):
        startnodes = self.findStartNode(self)
        endnodes = self.inputs[0].outputs
        endnodevalues = []
        for i in endnodes:
            endnodevalues.append(i.value)
        simOut = self.runSim()
        returnList = []
        for i in range(len(simOut)):
            returnList.append((simOut[i]-endnodevalues[i])**2)
        return returnList, startnodes
    def runSim(self):
        returnList = []
        for i in range(len(self.inputs)):
            returnList.append(self.inputs[i].runsim(iweights[i]))
        return returnList
    def adjust(self):
        pass

################ TEST AREA ##############

################ Functions ##############
    
def add(self,l):
    return sum(l)

def multiply(self,l):
    for i in l:
        prod*=i
    return prod

def inputweight(current, previousLayer):
    returnList = []
    for i in previousLayer:
        returnList.append(i.oWeights[current])
    return returnList

################ Layers ###################

inputLayer_info = [['node1',1],['node2',2],['node3',3]]
hiddenLayer_info = [['adder', add],['multiplier', multiply]]
outputLayer_info = [['node4',4],['node5',1]]

################ Layer Creation ###########

inputLayer = []
for i in inputLayer_info:
    inputLayer.append(InputNode(i[0], i[1], len(hiddenLayer_info)))
hiddenLayer = []
for i in range(len(hiddenLayer_info)):
    hiddenLayer.append(Node(hiddenLayer_info[i][0], inputLayer, inputweight(i,inputLayer), hiddenLayer_info[i][1], len(outputLayer_info))) 
outputLayer = []
for i in range(len(outputLayer_info)):
    outputLayer.append(OutputNode(outputLayer_info[i][0],outputLayer_info[i][1], hiddenLayer, inputweight(i,hiddenLayer)))
