'''
Created on Aug 30, 2016

@author: christianburkhartsmeyer
'''
from sys import argv
from frontend.parser import parseFile


print str(argv)

if len(argv) == 2 and argv[1] == '-h':
    print "412alloc Help:\nOptions:\n"
elif len(argv) == 3:
    #Lab 1
    if argv[1] == "-x":
        print "No register allocation, filename: " + argv[2]
        IR = parseFile(argv[2])
        # Traverse over links in IR
        while(IR.getNext() != None):
            print IR
            IR = IR.getNext()
    #Lab 2    
    elif ord(argv[1][0]) >= 48 and ord(argv[1][0]) <= 57:
        numRegisters = int(argv[1])
        print "Actual register allocation, filename: " + argv[2] + ", num registers: " + str(numRegisters)
else:
    print "Malformed arguments: " + str(argv) + ", use 412alloc -h for help"