# Try One at Neural Net for pattern recognition (c) Alex Shukhman, 2016
from math import *
from random import *
import json

global data
def read():
    with open ('data.json', 'r') as f:
        try:
            return json.load(f)
        except:
            return {}
data = read()

class Node:
    def __init__(self, name, inputnodes, iweights, function, outputNumber):
        self.inputs = inputnodes
        self.iws = iweights # from upstream nodes
        self.name = name
        self.function = function
        self.setupOWeights(outputNumber,0)
    def read(self):
        with open ('data.json', 'r') as f:
            data = json.load(f)
    def write(self):
        with open ('data.json', 'w') as f:
            json.dump(data, f)
    def setupOWeights(self, outputNumber,level):
        if data == {}:
            self.oWeights = []
            for i in range(outputNumber):
                self.oWeights.append(random())
        else:
            print ( data )
            minilist = []
            if level == 0:
                for i in range(outputNumber):
                    minilist.append(data[list(data.keys())[0]][2][self.name][0][i])
            else:
                for i in range(outputNumber):
                    minilist.append(data[list(data.keys())[i]][1][self.name])
            self.oWeights = minilist
    def findStartNode(self, node, previousNode):
        if node.inputs[0].findStartNode(node.inputs[0], node) == None:
            return node.inputs
        else:
            return node.inputs[0].findStartNode(node.inputs[0], node)
    def runSim(self,oweight):
        minilist = []
        for i in range(len(self.inputs)):
            minilist.append(self.inputs[i].runSim(self.iws[i]))
        self.fx = self.function(self,minilist)
        return oweight*self.fx
    def writeToData (self):
        wtdList = {}
        for i in self.inputs:
            wtdList[i.name] = i.writeToData()
        weightdic = {}
        for i in range(len(self.inputs)):
            weightdic[self.inputs[i].name] = self.iws[i]
        return weightdic, wtdList

class InputNode(Node):
    def __init__(self, name, value, outputNumber):
        self.name = name
        self.function = None
        self.iw = None
        self.inputs = {}
        self.value = value
        self.setupOWeights(outputNumber,1)
    def findStartNode(self,node,previousNode):
        return None
    def runSim(self,oweight):
        return self.value*oweight
    def writeToData(self):
        return self.value
    
class OutputNode(Node):
    def __init__(self, name, value, inputnodes, iweights):
        self.inputs = inputnodes
        self.name = name
        self.iws = iweights
        self.value = value
        self.function = None
        self.writeToData()
    def writeToData (self):
        wtdList = {}
        for i in self.inputs:
            wtdList[i.name] = i.writeToData()
        weightdic = {}
        for i in range(len(self.inputs)):
            weightdic[self.inputs[i].name] = self.iws[i]
        data[self.name] = self.value, weightdic, wtdList
    def findError(self):
        startnodes = self.inputs[0].findStartNode(self.inputs[0],self)
        endnodes = data.keys()
        endnodevalues = []
        for i in endnodes:
            endnodevalues.append(data[i][0])
        simOut = self.runSim()
        returnList = []
        for i in range(len(simOut)):
            returnList.append((simOut[i]-endnodevalues[i])**2)
        return returnList
    def runSim(self):
        returnList = []
        for i in range(len(self.inputs)):
            returnList.append(self.inputs[i].runSim(self.iws[i]))
        return returnList
    def adjust(self):
        pass

################ TEST BUILD AREA ########

################ Functions ##############
    
def add(self,l):
    return sum(l)

def multiply(self,l):
    prod = 1
    for i in l:
        prod*=i
    return prod

def inputweight(current, previousLayer):
    returnList = []
    for i in previousLayer:
        returnList.append(i.oWeights[current])
    return returnList

################ Layers ###################

inputLayer_info = [["node1",1],["node2",2],["node3",3]]
hiddenLayer_info = [["adder", add],["multiplier", multiply]]
outputLayer_info = [["node4",4],["node5",1]]

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

################ TEST EXECUTE AREA #########

outputLayer[0].write()
print(outputLayer[0].findError())
