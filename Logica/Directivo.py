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

