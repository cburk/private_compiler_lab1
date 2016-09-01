'''
Created on Aug 30, 2016

@author: christianburkhartsmeyer
'''

class IRLink(object):
    '''
    Linked list nodes
    '''

    def __init__(self, firstCmd):
        self.table = [None,firstCmd,0,0,0,float('inf'),0,0,0,float('inf'),0,0,0,float('inf'),None]

    #Pretty printing for final form
    #TODO: possible optimization, hashtable strings to ints for matching?
    #TODO: RN pulling ops from SR, for lab1 needs to be VR, for lab2 PR
    def __str__(self):
        table = self.table
        opName = table[1]
        retStr = opName
        #OP1
        firstOp = table[2]
        if firstOp != 0:
            retStr += "\t" + firstOp
        else:
            #NOP case
            return retStr
        #OP2/3
        if opName==("output"):
            return retStr
        elif opName == "loadl" or opName == "load":
            return retStr + "\t=>\t" + str(table[10])
        elif opName == "store":
            return retStr + "\t=>\t" + str(table[6])
        #arithop
        else:
            return retStr + "," + str(table[6]) + "\t=>\t" + str(table[10])
        


        #TODO: Change to be specific for each type, ex arithops need ,'s and most need =>
        #return str(self.table[1]) + " , " + str(self.table[2]) + " , " + str(self.table[6]) + " , " + str(self.table[10])
        
    def getPrev(self):
        return self.table[0]
    def getNext(self):
        return self.table[-1]
    def getTable(self):
        return self.table
    def setNext(self, a):
        self.table[-1] = a
    def setPrev(self, a):
        self.table[0] = a
    