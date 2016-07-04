# Try One at Neural Net for pattern recognition (c) Alex Shukhman, 2016
from math import *
from random import *

class Node:
    def __init__(self, name, inputnodes, iweight, function, outputNumber):
        self.inputs = inputnodes
        self.iw = iweight # from upstream nodes
        self.name = name
        self.function = classmethod(function)
        self.setOWeights()
    def setOWeights(self, outputNumber):
        self.oWeights = {}
        for i in range(outputNumber):
            self.oWeights[i] = random()
    def findStartNode(self, node, previousNode=None):
        if node.findStartNode(node, previousNode) == None:
            if previousNode != None:
                return previousNode.inputs
            else:
                return 'Started too far back'
        else:
            for i in self.inputs:
                return i.findStartNode(i,self)

class InputNode(Node):
    def __init__(self, name, value, outputNumber):
        self.inputs = {}
        self.iws = iweights
        self.value = value
        self.setOWeights(outputNumber)
    def findStartNode(self,node,previousNode=None):
        return None
    
class OutputNode(Node):
    def __init__(self, name, value, inputnodes, iweights):
        self.inputs = inputnodes
        self.outputs = {}
        self.iws = iweights
        self.value = value
    def findError(self):
        startnodes = self.findStartNode(self)
        endnodes = self.inputs[0].outputs
        endnodevalues = []
        for i in endnodes:
            endnodevalues.append(i.value)
        simout = self.runSim()
        returnList = []
        for i in range(len(simout)):
            returnList.append((simout[i]-endnodevalues[i])**2)
        return returnList, startnodes
    def adjust(self):
        pass

################ TEST ###################
def add(l):
    minilist = []
    for i in l:
        minilist.append(i.value*i.iw)
    return sum(l)

def multiply(l):
    minilist = []
    for i in l:
        minilist.append(i.value*i.iw)
    prod = 1
    for i in minilist:
        prod*=1
    return prod

def inputweight(current, previousLayer):
    returnList = []
    for i in previousLayer:
        returnList.append(i.oWeights[current])
    return returnList

inputLayer_info = [['node1',1],['node2',2],['node3',3]]
hiddenLayer_info = [['adder', add(l)],['multiplier', multiply(l)]]
outputLayer_info = [['node4',4],['node5',1]]
inputLayer = []
for i in inputLayer_info:
    inputLayer.append(InputNode(i[0], i[1], len(hiddenLayer_info)))
hiddenLayer = []
for i in range(len(hiddenLayer_info)):
    hiddenLayer.append(Node(hiddenLayer_info[i][0], inputLayer, inputweight(i,inputLayer), hiddenLayer_info[i][1], len(outputLayer_info))) 
outputLayer = []
for i in range(len(outputLayer_info)):
    outputLayer.append(OutputNode(outputLayer_info[i][0],outputLayer_info[i][1], hiddenLayer, inputweight(i,hiddenLayer)))
