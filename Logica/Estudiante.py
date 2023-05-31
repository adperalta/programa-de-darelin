class Estudiante:
    def __init__(self,ID, Name,LastN,Thesis):
        self.ID = ID
        self.Name = Name
        self.LastN = LastN
        self.Thesis = Thesis
    
    def getId(self):
        return self.ID
    
    def setId(self,ID):
        self.ID = ID
    
    def getName(self):
        return self.Name
    
    def setName(self,Name):
        self.Name = Name
    
    def getLastN(self):
        return self.LastN
    
    def setName(self,LastN):
        self.LastN = LastN