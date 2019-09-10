from MainMemory import MainMemory
import unittest


class MyTest(unittest.TestCase):
    def test_getData(self):
        dataInMem = testMemory.getData(1)
        self.assertEqual(dataInMem, "test")
    def test_storeData(self):
        testMemory.storeData(2, "test2")
        self.assertEqual(testMemory.memory[1], "test2")
        print(testMemory.memory)


if __name__ == "__main__":
    global testMemory
    testMemory = MainMemory()
    testMemory.memory[0] = "test"
    unittest.main()