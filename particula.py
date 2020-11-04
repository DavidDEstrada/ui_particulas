from algoritmos import distancia_euclidiana
class Particula:
    def __init__(self, iid = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, 
    red = 0, green = 0, blue = 0):
        self.__iid = iid
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

    
    def __str__(self):
        return(
          'Id: ' + str(self.__iid)+ '\n'+
          'Origen en x: ' + str(self.__origen_x)+'\n'+
          'Origen en y: ' + str(self.__origen_y)+'\n'+
          'Destino en x: ' + str(self.__destino_x)+'\n'+
          'Destino en y: ' + str(self.__destino_y)+'\n'+
          'Velocidad: ' + str(self.__velocidad)+'\n'+
          'Red: ' + str(self.__red)+'\n'+
          'Green: ' + str(self.__green)+'\n'+
          'Blue: ' + str(self.__blue)+'\n'+
          'Distancia: ' + str(self.distancia)+ '\n'
        )
    
    def to_dict(self):
        return {
          "iid": self.__iid,
          "origen_x": self.__origen_x,
          "origen_y": self.__origen_y,
          "destino_x": self.__destino_x,
          "destino_y": self.__destino_y,
          "velocidad": self.__velocidad,
          "red": self.__red,
          "green": self.__green,
          "blue": self.__blue
        }