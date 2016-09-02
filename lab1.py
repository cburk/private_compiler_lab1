'''
Created on Aug 30, 2016

@author: christianburkhartsmeyer
'''
from sys import argv
from frontend.parser import parseFile
from backend.virtualizer import renameVirtRegisters


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
        numRegisters = int(argv[1])
        print "Actual register allocation, filename: " + argv[2] + ", num registers: " + str(numRegisters)
elif len(argv) == 2 and argv[1] == '-h':
    print """412alloc Help:\nOptions:\n
               """
else:
    print "Malformed arguments: " + str(argv) + ", use 412alloc -h for help"