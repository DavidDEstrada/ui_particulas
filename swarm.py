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
    
    def __str__(self):
        return "".join (

            str(particula) + "\n" for particula in self.__swarm

        )