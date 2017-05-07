# *-* encoding: utf-8 *-*

class Dia:
    def __init__ (self,horas,minuto,segundo):
        self.hora = horas
        self.min = minuto
        self.seg = segundo
    def manania(self):
        estado = False
        if self.hora>=6 and self.hora <12:
            estado = True
        return estado
    def tarde(self):
        estado = False
        if self.hora>=12 and self.hora <=18:
            estado = True
        return estado
    def noche(self):
        estado = False
        if self.hora>=18 and self.hora <=6:
            estado = True
        return estado