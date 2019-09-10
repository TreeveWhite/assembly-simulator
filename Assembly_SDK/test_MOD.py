import unittest
from MOD import MOD

class MyTest(unittest.TestCase):

    def setUp(self):
        self.cpu = CPU()
        self.mem = testMemory()
        self.testCommand = MOD("MOD R1, #12", self.mem, self.cpu)
        return super().setUp()

    def test_init(self):
        self.assertEqual(self.testCommand.opcode, "MOD")
        self.assertEqual(self.testCommand.operand, ["R1", "#12"])

    def test_getValue(self):
        newTest = self.testCommand.getValue(self.mem)
        self.assertEqual(newTest, "12")
    
    def test_getRegister(self):
        newTest = self.testCommand.getRegister()
        self.assertEqual(newTest, 1)

class testMemory:
    def __init__(self):
        self.testMem = []
    def getData(self, location):
        try:
            data = self.testMem[location - 1]
            return data
        except:
            return "No Data in Location"

class CPU:
    def __init__(self):
        self.registers = [None, None, None, None, None, None, None, None]
        self.programCounter = 0

if __name__ == "__main__":
    
    unittest.main()
