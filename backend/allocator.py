'''
Created on Sep 4, 2016

@author: christianburkhartsmeyer
'''

VRToPR = []
PRToVR = []
NextUse = []


def allocatePRS(firstInstr, numVRs, numPRs):
    global VRToPR
    global PRToVR
    global NextUse
    
    # TODO: Should i subtract one from numPR's for spilling?
    
    VRToPR = [-1] * numVRs
    PRToVR = [-1] * numPRs
    NextUse = [-1] * numPRs
    
    curInstr = firstInstr
    j = 0
    while curInstr.getNext() != None:
        print "Inst: " + str(j)
        j += 1
        
        thisTable = curInstr.getTable()
        PROP1 = -1
        PROP2 = -1
        
        #Handle OP1, only memop and arithop have r1
        print " = loadl? " + str(thisTable[1])
        if thisTable[1] != "nop" and thisTable[1] != "output" and thisTable[1] != "loadl" :
            op1VR = thisTable[3]
            op1NextUse = thisTable[5]
            #See if there's a free PR
            freePR = -1
            for i in range(numPRs):
                if PRToVR[i] == -1 or PRToVR[i] == op1VR:
                    freePR = i
                    break
            # If there wasn't, spill the one with the furthest next use
            if freePR == -1:
                farthestPR = 0
                usedAt = NextUse[0]
                for i in range(numPRs - 1):
                    # TODO: Should I choose which to spill arbitrarily when equal?  Slides
                    if NextUse[1 + i] > usedAt:
                        farthestPR = 1 + i
                        usedAt = NextUse[1 + i]
                spilledVR = PRToVR[farthestPR]
                print "Had to spill for op 1, spilling PR: " + str(farthestPR) + " , which is VR: " + str(spilledVR) + ", which is next used at: " + str(usedAt)
                # TODO: Spill
                freePR = farthestPR
                VRToPR[spilledVR] = -1
            
            PRToVR[freePR] = op1VR
            NextUse[freePR] = op1NextUse
            PROP1 = freePR
            
            print "OP 1, vr: " + str(op1VR) + " in vr: " + str(freePR)
                            
            # Keep track of 
            thisTable[4] = freePR

        #Handle OP2
        if thisTable[1] == "add" or thisTable[1] == "sub" or thisTable[1] == "mult" or thisTable[1] == "lshift" or thisTable[1] == "rshift": 
            op2VR = thisTable[7]
            op2NextUse = thisTable[9]
            
            #See if there's a free PR
            freePR = -1
            for i in range(numPRs):
                if PRToVR[i] == -1 or PRToVR[i] == op2VR:
                    freePR = i
                    break
            # If there wasn't, spill the one with the furthest next use
            # TODO: Do we need to 
            if freePR == -1:
                farthestPR = 0
                usedAt = NextUse[0]
                for i in range(numPRs - 1):
                    # TODO: Should I choose which to spill arbitrarily when equal?  Slides
                    if NextUse[1 + i] > usedAt:
                        farthestPR = 1 + i
                        usedAt = NextUse[1 + i]
                spilledVR = PRToVR[farthestPR]
                print "Had to spill for OP2, spilling PR: " + str(farthestPR) + " , which is VR: " + str(spilledVR) + ", which is next used at: " + str(usedAt)
                # TODO: Spill
                freePR = farthestPR
                VRToPR[spilledVR] = -1
                
            PRToVR[freePR] = op2VR
            NextUse[freePR] = op2NextUse
            PROP2 = freePR
            
            print "OP 2, vr: " + str(op2VR) + " in vr: " + str(freePR)
                        
            # Keep track of 
            thisTable[8] = freePR
            
        # Free PR's for 1/2 if NextUse is 0
        if PROP1 != -1 and op1NextUse == float("inf"):
            print "OP 1 inf next use"
            VRToPR[op1VR] = -1
            PRToVR[PROP1] = -1
            NextUse[PROP1] = float("inf")
        
        if PROP2 != -1 and op2NextUse == float("inf"):
            print "OP 2 inf next use"
            VRToPR[op2VR] = -1
            PRToVR[PROP2] = -1
            NextUse[PROP2] = float("inf")
            
        #Handle OP3
        if thisTable[1] != "output" and thisTable[1] != "nop":
            if thisTable[1] == "load":
                op3VR = thisTable[7]
                op3NextUse = thisTable[9]
            else:
                op3VR = thisTable[11]
                op3NextUse = thisTable[13]
                
            print "Op 3: " + str(op3VR)
            print thisTable
            
            #See if there's a free PR
            freePR = -1
            for i in range(numPRs):
                if PRToVR[i] == -1 or PRToVR[i] == op3VR:
                    freePR = i
                    break
            # If there wasn't, spill the one with the furthest next use
            # TODO: Do we need to 
            if freePR == -1:
                farthestPR = 0
                usedAt = NextUse[0]
                for i in range(numPRs - 1):
                    # TODO: Should I choose which to spill arbitrarily when equal?  Slides
                    if NextUse[1 + i] > usedAt:
                        farthestPR = 1 + i
                        usedAt = NextUse[1 + i]
                spilledVR = PRToVR[farthestPR]
                print "Had to spill for OP3, spilling PR: " + str(farthestPR) + " , which is VR: " + str(spilledVR) + ", which is next used at: " + str(usedAt)
                # TODO: Spill
                freePR = farthestPR
                VRToPR[spilledVR] = -1
            
            
            PRToVR[freePR] = op3VR
            NextUse[freePR] = op3NextUse
            
            print "OP 3, vr: " + str(op3VR) + " in vr: " + str(freePR)
            
            # Keep track of 
            if thisTable[1] != "load":
                thisTable[12] = freePR
            else:
                thisTable[8] = freePR
            
        print "PR's: " + str(PRToVR)
        
        
        curInstr = curInstr.getNext()
    """
    for eachInstr:
        if OP1 used in instruction:
            if OP1 needs register:
                get one
            # If it's dead, free it
            if OP1.NU == INF:
                reset
            
        if OP2...
        
        if OP3...
    
    """
    
    return 0