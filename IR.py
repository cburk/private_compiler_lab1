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

    def __str__(self):
        #TODO: Change to be specific for each type, ex arithops need ,'s and most need =>
        return str(self.table[1]) + " , " + str(self.table[2]) + " , " + str(self.table[6]) + " , " + str(self.table[10])
        
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
    