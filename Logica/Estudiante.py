class Estudiante:
    def __init__(self,IDEst,Name,Sex,LastN,Thesis):
        self.ID = IDEst
        self.Sex = Sex
        self.Name = Name
        self.LastN = LastN
        self.Thesis = Thesis
    
    def getId(self):
        return self.IDEst
    
    def setId(self,IDEst):
        self.IDEst = IDEst
    
    def getSex(self):
        return self.Sex
    
    def setId(self,Sex):
        self.Sex = Sex
    
    def getName(self):
        return self.Name
    
    def setName(self,Name):
        self.Name = Name
    
    def getLastN(self):
        return self.LastN
    
    def setLastN(self,LastN):
        self.LastN = LastN