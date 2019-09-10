from Enums import AssemblyLang
from MOD import MOD
from STR import STR

class CommandAnalyser(object):

    """ A Class which analyses each line of code to the  be sorted to the correct command class """

    def __init__(self, code, memory, cpu):
        self.code = code
        self.type = self.getType()
        self.sortCommand(memory, cpu)
    
    def getType(self):
        if self.code[0] == "B" and self.code[1] == " ":
            return AssemblyLang.B
        opcode = self.code[0:3]
        if opcode == "MOD":
            return AssemblyLang.MOD
        elif opcode == "STR":
            return AssemblyLang.STR       

    def sortCommand(self, memory, cpu):
        if self.type == AssemblyLang.MOD:
            self.commandMethod = MOD(self.code, memory, cpu)
        elif self.type == AssemblyLang.STR:
            self.commandMethod = STR(self.code, memory, cpu)

        
        