class Media:
    def __init__(self,Nome,Nota1,Nota2,Nota3):
        self.Nome = Nome
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Nota3 = Nota3

    def Calcular_media(self):
        Media = (int(self.Nota1) + int(self.Nota2) + int(self.Nota3)) /3
        
        return Media
        
    def __str__(self):
        return f"{self.Nome} Media: {self.Calcular_media()}"