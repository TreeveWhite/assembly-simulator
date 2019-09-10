

class STR(object):

    """ A Class for any STR statements in Assembly Code """

    def __init__(self, code, memory, cpu):
        self.code = code
        self.opcode = code[0:3]
        self.operand = code[3: len(self.code)].replace(" ", "").split(",")

        data = self.getDataFromReg(cpu)

        self.storeDataInMem(data, memory)

        cpu.programCounter += 1

    def getDataFromReg(self, cpu):
        data = str(cpu.registers[int(self.operand[0][1])-1])
        return data
    
    def storeDataInMem(self, data, memory):
        location = int(self.operand[1])
        memory.storeData(location, data)
