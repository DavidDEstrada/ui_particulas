from particula import Particula
import json

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