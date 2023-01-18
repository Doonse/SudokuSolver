

class Square:

    def __init__(self, nums):
        self.num = None
        self.connections = [None, None, None]

    def setNumber(self, number):
        self.num = number
    
    def setConnections(self, connections):
        self.connections = connections

    def getNumber(self):
        return self.num

    def getConnections(self):
        return self.connections

    def __str__(self):
        return str(self.num)


