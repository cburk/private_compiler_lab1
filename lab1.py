'''
Created on Aug 30, 2016

@author: christianburkhartsmeyer
'''
from sys import argv
from frontend.parser import parseFile
from backend.virtualizer import renameVirtRegisters
from IR import IRLink
from backend.allocator import allocatePRS

print "Hello world!"

if len(argv) == 3:
    #Check 1
    if argv[1] == "-x":
        #print "No register allocation, filename: " + argv[2]
        firstLast = parseFile(argv[2])
        IRInst1 = firstLast[0]
        IRInstFinal = firstLast[1]
        numLines = firstLast[2]
        maxVRNum = firstLast[3]
        # Traverse over links in IR, comment out
        """
        curInst = IRInst1
        while(curInst != None):
            print curInst
            curInst = curInst.getNext()
        """
            
        #Renaming, live ranges
        renameVirtRegisters(IRInst1, IRInstFinal, numLines, maxVRNum)
        #print "Returned from renaming successfully"
        curInst = IRInst1
        while(curInst != None):
            print curInst
            curInst = curInst.getNext()
        
        
    #Check 2    
    elif ord(argv[1][0]) >= 48 and ord(argv[1][0]) <= 57:
        """
        numRegisters = int(argv[1])
        print "Actual register allocation, filename: " + argv[2] + ", num registers: " + str(numRegisters)
        
        # Scan and parse file, front end
        firstLast = parseFile(argv[2])
        IRInst1 = firstLast[0]
        IRInstFinal = firstLast[1]
        numLines = firstLast[2]
        maxVRNum = firstLast[3]
        
        
        #Renaming to virt registers, fill in live ranges
        renameVirtRegisters(IRInst1, IRInstFinal, numLines, maxVRNum)
        """
        #Perform actual register allocation
        myIR = [[None,'loadl',128,0,0,float('inf'),0,0,0,0,0,1,0,1,None],
                [None,'load',0,1,0,8,0,2,0,7,0,0,0,0,None],
                [None,'loadl',132,0,0,float('inf'),0,0,0,0,0,7,0,3,None],
                [None,'load',0,7,0,float('inf'),0,4,0,6,0,0,0,0,None],
                [None,'loadl',136,0,0,float('inf'),0,0,0,0,0,6,0,5,None],
                [None,'load',0,6,0,float('inf'),0,5,0,6,0,0,0,0,None],
                [None,'mult',0,4,0,float('inf'),0,5,0,float('inf'),0,3,0,7,None],
                [None,'add',0,2,0,float('inf'),0,3,0,float('inf'),0,0,0,8,None],
                [None,'store',0,0,0,float('inf'),0,1,0,float('inf'),0,0,0,0,None],]
        
        inIRForm = []
        prev = None
        i = 0
        for table in myIR:
            this = IRLink(table, True)
            this.setPrev(prev)
            if i > 0:
                prev.setNext(this)
            prev = this
            inIRForm.append(this)
            i += 1
            
        allocatePRS(inIRForm[0], 8, 4)
            
            
        """
        for newIR in inIRForm:
            print newIR
        """
        
        
elif len(argv) == 2 and argv[1] == '-h':
    print """412alloc Help:\nOptions:\n
               """
else:
    print "Malformed arguments: " + str(argv) + ", use 412alloc -h for help"