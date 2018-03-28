###########################################
# Arman Ashrafian
# March 2018

# SAP-1 Assembler
###########################################

import sys

# Intructions:
# LDA - 0000 (Load A register)
# ADD - 0001 (Add A & B register, store in A)
# SUB - 0010 (A-B, store in B)
# OUT - 1110 (Output contents of register A)
# HLT - 1111 (Halt program execution)
instructions = {
    'LDA': '0000',
    'ADD': '0001',
    'SUB': '0010',
    'OUT': '1110',
    'HLT': '1111',
}

def main():
    # get filename from args
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    else: 
        print("Error: need file to assemble")
        return # end program

    print("Assembling...")

    # read & tokenize file
    code = readFile(filename).upper()
    tokens = tokenize(code)
    obj = parse(tokens)

    outputObj(obj)

def readFile(filename):
    try:
        with open(filename, 'r') as fil:
            code = fil.read()
    except:
        print("Error: no source code")
        sys.exit(0)
    return code

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
                obj.append(instructions[line[0]])
                obj.append('\n')
            # Error if instruction is invalid
            except KeyError:
                print('Error Line %d - invalid instruction' % lineNumber)
                sys.exit(0)
            # Error if instruction is not HLT or not OUT
            if line[0] != 'HLT' and line[0] != 'OUT': 
                print('Error Line %d - expecting parameter' % lineNumber)
                sys.exit(0)

        # Instructions with parameter
        else:
            # Error if HLT or OUT has a parameter
            if line[0] == 'HLT' or line[0] == 'OUT':
                print('Error Line %d - invalid parameter' % lineNumber)
                sys.exit(0)
            # Error if invalid parameter
            if not isValidParam(line[1]):
                print('Line %d - invalid parameter' % lineNumber)
                sys.exit(0)
            try:
                obj.append(instructions[line[0]])
                obj.append(line[1])
                obj.append('\n')
            except:
                print('Line %d - invalid instruction' % lineNumber)
                sys.exit(0)
        lineNumber += 1

    return obj

def isValidParam(param):
    ''' true if param is between 0000 - 1111 '''
    # check length
    if len(param) != 4: return False
    # check 0 <= param <= 15
    for char in param:
        if not (char == '1' or char == '0'):
            return False
    return True

def outputObj(obj):
    fOut = open(('%s.out' % sys.argv[1].split('.')[0]), 'w')
    for e in obj:
        fOut.write(e)
    fOut.close()

def testValidParam():
    one = '0001'
    two = '0010'
    three = '0011'

    print(isValidParam(one))
    print(isValidParam(two))
    print(isValidParam(three))


if __name__ == '__main__':
    main()