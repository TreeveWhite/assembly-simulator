from CPU import CPU
from CommandAnalyser import CommandAnalyser
from MainMemory import MainMemory




if __name__ == "__main__":
    
    code = ["MOD R1, #55", "STR R1, 1"]
    cpu = CPU()
    mainMemory = MainMemory()

    x = 0

    while not cpu.codeCompleted:
        analysedComand = CommandAnalyser(code[cpu.programCounter], mainMemory, cpu)
        command = analysedComand.commandMethod

        x += 1
        if x >= len(code):
            cpu.codeCompleted = True
            
    print(cpu.registers)
    print(mainMemory.memory)