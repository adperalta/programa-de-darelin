class Directivo():
    def __init__(self,IDdir,Name,Sex,Puesto,):
        self.ID = IDdir
        self.Name = Name
        self.Sex = Sex
        self.Puesto = Puesto
    
    def getId(self):
        return self.IDdir
    
    def setId(self,IDdir):
        self.IDdir =  IDdir 

    def getName(self):
        return self.Name
    
    def setId(self,Name):
        self.Name =  Name

    def getSex(self):
        return self.Sex
    
    def setId(self,Sex):
        self.Sex =  Sex

    def getPuesto(self):
        return self.Puesto
    
    def setPuesto(self,Puesto):
        self.Puesto =  Puesto