

class MOD(object):

    """ A Class for any MOD Statements in the Assembly Code """

    def __init__(self, code, memory, cpu):
        self.code = code
        self.opcode = code[0: 3]
        self.operand = code[3: len(self.code)].replace(" ", "").split(",")

        self.value = self.getValue(memory)
        
        self.targetReg = self.getRegister()

        self.updateReg(cpu)

        cpu.programCounter += 1

    def getValue(self, memory):
        if self.operand[1][0] == "#":
            value = self.operand[1][1: len(self.operand)+1]

            return value

        else:
            value = memory.getData(self.operand[1][0])


    def getRegister(self):
        register = int(self.operand[0][1])
        return register
    
    def updateReg(self, cpu):
        cpu.registers[self.targetReg-1] = str(self.value)