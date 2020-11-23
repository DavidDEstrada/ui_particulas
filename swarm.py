from particula import Particula
import json


def ordenar_by_distancia(particula):
        return particula.distancia


class Swarm:
    def __init__(self):
        self.__swarm = []
    
    def ordenar_id(self):
        self.__swarm.sort()
    
    def ordenar_distancia(self):
        self.__swarm.sort(key= ordenar_by_distancia, reverse=True)
    
    def ordenar_velocidad(self):
        self.__swarm.sort(key= lambda particula: particula.velocidad)

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
    def __len__(self):
        return len(self.__swarm)
    
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__swarm):
            particula = self.__swarm[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__swarm]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__swarm = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0