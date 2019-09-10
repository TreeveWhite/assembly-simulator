

class MainMemory(object):

    """ Class for Main Memory, all stored in main memory as a string"""

    def __init__(self):
        self.memory = []
        for i in range(100):
            self.memory.append("")
    
    def getData(self, location):
        data = self.memory[location - 1]
        return data
    
    def storeData(self, location, data):
        self.memory[location-1] = str(data)