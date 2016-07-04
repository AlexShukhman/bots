# Try One at Neural Net for pattern recognition (c) Alex Shukhman, 2016
from math import *
from random import *

class Node:
    def __init__(self, value, name, inputnodes, outputnodes, iweights, function):
        self.inputs = inputnodes
        self.outputs = outputnodes
        self.iws = iweights # from upstream nodes
        self.value = value
        self.name = name
        self.function = classmethod(function)
        self.setOWeights()
    def setOWeights(self):
        self.oWeights = {}
        for i in self.outputs:
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
    def __init__(self, value, name):
        self.inputs = {}
        self.iws = iweights
        self.value = value
        self.setOWeights()
    def findStartNode(self,node,previousNode=None):
        return None
    
class OutputNode(Node):
    def __init__(self, value, name, inputnodes, iweights, oweights):
        self.inputs = inputnodes
        self.outputs = {}
        self.iws = iweights
        self.value = value
    def findError(self):
        startnodes = self.findStartNode(self)
        endnodes = self.inputs[i].outputs
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

inputLayer = [{2,1,]
