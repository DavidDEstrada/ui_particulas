from particula import Particula

class Swarm:
    def __init__(self):
        self.__swarm = []

    def agregar_final(self, particula:Particula):
        self.__swarm.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__swarm.insert(0 , particula)
    
    def mostrar(self):
        for particula in self.__swarm:
            print(particula)

p01 = Particula(iid = 1, origen_x = 2, origen_y = 3, destino_x = 4, destino_y = 5, velocidad = 6, 
    red = 7, green = 8, blue = 9)
p02 = Particula(22,33,44,55,66,77,222,233,224)

swarm = Swarm()

swarm.agregar_final(l01)
swarm.agregar_inicio(l02)
swarm.agregar_inicio(l01)
swarm.mostrar()