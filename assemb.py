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
        print("Error: Need file to assemble")
        return # end program

    print("Assembling...")

    # read & tokenize file
    code = readFile(filename)
    tokens = tokenize(code)
    obj = parse(tokens)

    outputObj(obj)

def readFile(filename):
    try:
        with open(filename, 'r') as fil:
            code = fil.read()
    except:
        raise Exception("No Source Code")
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
            except KeyError:
                raise Exception('Line %d - Invalid Instruction' % lineNumber)
            except: 
                raise Exception('Line %d - Unexpected Parameter' % lineNumber)
        # Instructions with parameter
        else:
            try:
                valid = isValidParam(line[1])
                obj.append(instructions[line[0]])
                obj.append(line[1])
                obj.append('\n')
            except:
                if not valid: raise Exception('Line %d - Invalid Parameter' % lineNumber)
                else: raise Exception('Line %d - Invalid Instruction' % lineNumber)

        lineNumber += 1
    return obj

def isValidParam(param):
    ''' true if param is between 0000 - 1111 '''
    if len(param) != 4: return False
    for char in param:
        if char != '1' or char != '0':
            return False
    return True

def outputObj(obj):
    fOut = open(('%s.out' % sys.argv[1].split('.')[0]), 'w')
    for e in obj:
        fOut.write(e)
    fOut.close()



if __name__ == '__main__':
    main()