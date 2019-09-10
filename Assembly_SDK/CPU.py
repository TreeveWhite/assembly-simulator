
from MainMemory import MainMemory

class CPU:
    
    """ A Class to hold all data that would be stored in the CPU (ALL STORED AS STR)"""
    
    def __init__(self):
        self.registers = [None, #R1
                          None, #R2
                          None, #R3
                          None, #R4
                          None, #R5
                          None, #R6
                          None, #R7
                          None] #R8
        self.programCounter = 0
        self.codeCompleted = False
    
    def changeRegister(self, newValue, register, mainMemory = None): 
        if newValue[0] == "#":
            self.registers[register-1] = str(newValue[0:len(newValue)])

        else:
            data = mainMemory.getData(newValue)
            self.registers[register-1] = str(data)
