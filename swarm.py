from particula import Particula
import json
from pprint import pformat
from collections import deque

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
    
    def crear_grafo(self):
        d = {} 
        for particula in self.__swarm: 
                    
            origen = particula.origen_x, particula.origen_y
            destino = particula.destino_x, particula.destino_y
            distancia = particula.distancia

            arista_o_d = (destino, distancia)
            arista_d_o = (origen, distancia)

            if origen in d:
                d[origen].append(arista_o_d)
            else:
                d[origen] = [arista_o_d]
            if destino in d:
                d[destino].append(arista_d_o)
            else:
                d[destino] = [arista_d_o]
            
        return d
    
    def ver_grafos(self):
                d = self.crear_grafo()
                grafo = pformat(d, width=40, indent=1)
                return grafo
    
    def quitar_peso(self):
            d = self.crear_grafo()
            d2 = d.copy()
            for i in d:
                d2[i] = [x[0] for x in d[i]]
            return d2

    def algoritmo_busqueda_profundidad(self,origen):

            d2 = self.quitar_peso()
            visitados = deque()
            pila = deque()
            recorrido = deque()

            visitados.append(origen)
            pila.append(origen)

            while len(pila) > 0:
                vertice = pila[-1]
                recorrido.append(vertice)
                pila.pop()  

                adyacentes = d2[vertice]
                for i in adyacentes:
                    ady = i
                    if ady not in visitados:
                        visitados.append(ady)
                        pila.append(ady)

            return recorrido

    def algoritmo_busqueda_Amplitud(self,origen):
            d2 = self.quitar_peso()
            visitados = deque()
            cola = deque()
            recorrido = deque()

            visitados.append(origen)
            cola.append(origen)

            while len(cola) > 0:
                vertice = cola[0]
                recorrido.append(vertice)
                del cola[0]

                adyacentes = d2[vertice]
                for i in adyacentes:
                    ady = i
                    if ady not in visitados:
                        visitados.append(ady)
                        cola.append(ady)    

            return recorrido