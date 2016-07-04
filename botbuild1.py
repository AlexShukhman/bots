
# Bot Build 1

'''
A simple learning bot that has the capacity to guess which source is correct by its level of trust in each source

This bot uses geometric conservatism bias and will weigh the initial data more than later data
    Bot's level of conservatism bias is positively correlated (>dep value --> >bias)
    Conservatism bias is set initially in initialization as dep
        eg: Bot = LearningBot(dep = x)

This bot exibits illusion of validity starting at initilization (it believes everything it hears)

This bot allows for different administrative strength
    (one can ovverride conservatism biases by changing influence strength when running teachtruthes method)
'''

# (c) Alex Shukhman: July 3, 2016

'''

Change Log:



'''
##################################################################
##################################################################

class LearningBot:
    def __init__(self, dep = 1.5, truthesmem = [], truthesbelief = {}):
        self.initbelief = 1
        self.belief = self.initbelief # current level of disbelief
        self.dep = dep # how fast belief depreciates
        self.truthesmem = truthesmem # a list of 4 element lists of 2 element lists, first element is the input (4 possibilities), second is its value
        self.truthesbelief= truthesbelief.copy() # a dictionary of weighted belief in each input
        self.truthesbelief_tot = truthesbelief.copy()
    def teachtruthes(self,info,influence = 1): # info is a list of 4 elements of len2 lists, influence is a value <=1
        self.truthesmem.append(info)
        self.thinktruthes(info, influence)
    def evenate(self,d): # sets total of dictionary values to 1
        total = 0
        dic = d.copy()
        for i in dic.keys():
            total += dic[i]
        for i in dic.keys():
            try:
                dic[i] /= total
            except:
                dic[i] = 0
        return dic
    def thinktruthes(self,info,influence): # data processing
        beliefdict = {}
        for i in range(len(info)-1):
            if info[-1][1] == info[i][1]:
                try:
                    beliefdict[info[i][0]]+=1
                except:
                    beliefdict[info[i][0]]=1
        for i in range(len(info)-1):
            if info[i][0] not in beliefdict.keys():
                beliefdict[info[i][0]] = 0
        beliefdict = self.evenate(beliefdict)
        for i in beliefdict.keys():
            if i in self.truthesbelief_tot.keys():
                self.truthesbelief_tot[i]+=((beliefdict[i]/self.belief)*influence)
            else:
                self.truthesbelief_tot[i]=((beliefdict[i]/self.belief)*influence)

        self.truthesbelief = self.evenate(self.truthesbelief_tot)
        self.belief /= self.dep

def represent(i):
    return i
botA = LearningBot(dep = 1.2)
a = 'a'
info = [[[1,1],[2,0],[3,1],[a,1]],[[4,1],[2,0],[3,1],[a,1]],[[3,1],[2,1],[4,0],[a,0]],[[1,0],[2,1],[3,1],[a,0]],[[1,1],[2,0],[3,1],[a,0]],[[5,0],[2,1],[3,1],[a,0]],[[1,0],[2,1],[3,1],[a,0]]]
for i in info:
    botA.teachtruthes(i)

print (botA.truthesbelief)
