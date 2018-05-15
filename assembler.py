###########################################
# Arman Ashrafian
# March 2018

# SAP-1 Assembler
###########################################

import sys

# 4 bit Dec -> Bin
decToBin = {
    0:  '0000',
    1:  '0001',
    2:  '0010',
    3:  '0011',
    4:  '0100',
    5:  '0101',
    6:  '0110',
    7:  '0111',
    8:  '1000',
    9:  '1001',
    10: '1010',
    11: '1011',
    12: '1100',
    13: '1101',
    14: '1110',
    15: '1111',
}

# SAP-1 Intruction Set
instructionsNoParam = {
    'NOOP': '0000',
    'OUT':  '1110',
    'HLT':  '1111',
    '0000': 'NOOP',
    '1110': 'OUT',
    '1111': 'HLT',
}

instructionsWithParam = {
    'LDA':  '0001',
    'ADD':  '0010',
    'SUB':  '0011',
    'STA':  '1111',
    'LDI':  '0101',
    'JMP':  '0110',
    'JC':   '0111',
    'JZ':   '1000',
    '0001': 'LDA',
    '0010': 'ADD',
    '0011': 'SUB',
    '1111': 'STA',
    '0101': 'LDI',
    '0110': 'JMP',
    '0111': 'JC',
    '1000': 'JZ',
}

def tokenize(code):
    ''' create a 2D array of instructions by line '''
    split1 = code.split('\n')
    split2 = []
    for x in split1:
        split2.append(x.split())
    return split2

def parse(tokens):
    obj = []
    lineNumber = 1
    for line in tokens:
        # Instructions with no parameter
        if len(line) == 1:
            try: 
                obj.append(instructionsNoParam[line[0]])
                obj.append('\n')
            # Error if instruction is invalid
            except KeyError:
                return 'Error Line %d - invalid instruction' % lineNumber

        # Instructions with parameter
        else:
            if line[0] not in instructionsWithParam:
                return 'Error Line %d - %s does not recieve an argument' % (lineNumber, line[0])
            # Error if invalid parameter
            if not isValidParam(int(line[1])):
                return 'Line %d - invalid parameter' % lineNumber
            try:
                obj.append(instructionsWithParam[line[0]])
                obj.append(decToBin[int(line[1])])
                obj.append('\n')
            except:
                return 'Line %d - invalid instruction' % lineNumber
        lineNumber += 1

    return obj

def isValidParam(param):
    return (param >= 0 and param <= 15)

def binaryToDec(binstr):
    ''' convert 4 bit binary to decimal '''
    n = 3
    val = 0
    for i in binstr:
        if i == '1':
            val += 2 ** (n)
        n -= 1
    return val

def disassemble(tokens):
    asm = []
    for line in tokens:
        if len(line) == 0: continue
        # NO PARAMETER
        if len(line[0]) == 4:
            try:
                instruc = instructionsNoParam[line[0]]
                asm.append(instruc)
            except KeyError:
                return 'Error - Corrupt Binary'
        # WITH PARAMETER
        elif len(line[0]) == 8:
            try:
                instruc = instructionsWithParam[line[0][0:4]]
                param  = binaryToDec(line[0][4:])
                asm.append("%s %d" % (instruc, param))
            except KeyError:
                return 'Error - Corrupt Binary'
        else:
            return 'Error - Corrupt Binary'
    return asm


