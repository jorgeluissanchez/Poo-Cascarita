from __future__ import annotations
from typing import List
from enum import Enum
from abc import ABC

class RockRollRadio:

    def __init__(self) -> None:
        self.__artistas: List["Artista"] = []
        self.__canciones: List["Cancion"] = []
        self.__invitados: List["Invitado"] = []
        self.__locutores: List["Locutor"] = []
        self.__programas: List["Programa"] = []

    @property
    def artistas(self) -> List["Artista"]:
        return self.__artistas
        
    @property
    def canciones(self) -> List["Cancion"]:
        return self.__canciones
    
    @property
    def invitados(self) -> List["Invitado"]:
        return self.__invitados
    
    @property
    def locutores(self) -> List["Locutor"]:
        return self.__locutores
        
    @property
    def programas(self) -> List["Programa"]:
        return self.__programas
    
    def add_locutor(self, locutor: "Locutor") -> bool:
        self.__locutores.append(locutor)
        return True
    
    def add_programa(self, programa: "Programa") -> bool:
        self.__programas.append(programa)
        return True
    
    def add_artista(self, artista: "Artista") -> bool:
        self.__artistas.append(artista)
        return True
    
    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    
    def add_emision(self, emision: "Emision") -> bool:
        return True

    def add_invitado(self, invitado: "Invitado", emision: "Emision") -> bool:
        self.__invitados.append(invitado)
        invitado.add_emision(emision)
        emision.add_invitado(invitado)
        return True
    
    # ahora no
    def get_programa_con_mas_canciones_de_artista(self, artista: "Artista") -> "Programa":
        frecuencia = {}
        for programa in self.__programas:
            frecuencia[programa] = programa.get_frecuencia_canciones(artista)
        return max(frecuencia, key = frecuencia.get)

class Persona(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
  
class Locutor(Persona):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__programas: List["Programa"] = []

    def add_programa(self, programa: "Programa") -> bool:
        self.__programas.append(programa)
        return True

class Programa:

    __ID = 1

    def __init__(self, nombre: str, locutor: "Locutor") -> None:
        self.__nombre = nombre
        self.__serial = Programa.__ID
        self.__emisiones: List["Emision"] = []
        self.__locutores: List["Locutor"] = [locutor]

        self.__locutores[0].add_programa(self)

        Programa.__ID += 1

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    def add_emision(self, emision: "Emision") -> bool:
        self.__emisiones.append(emision)
        return True
    
    def get_last_emision(self) -> "Emision":
        return self.__emisiones[-1]
    # ahora no
    def get_frecuencia_canciones(self, artista: "Artista") -> int:
        frecuencia = 0
        for emision in self.__emisiones:
            frecuencia += emision.get_cantidad_canciones(artista)
        return frecuencia

class Emision:
    __ID = 1
    def __init__(self, programa: "Programa") -> None:
        self.__serial = Emision.__ID
        self.__canciones: List["Cancion"] = []
        self.__invitados: List["Invitado"] = []
        self.__programa = programa

        self.__programa.add_emision(self)

        Emision.__ID += 1

    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    
    def add_invitado(self, invitado: "Invitado") -> bool:
        self.__invitados.append(invitado)
        return True
    
    def get_cantidad_canciones(self, artista: "Artista") -> int:
        canciones = [cancion for cancion in self.__canciones if cancion.artista == artista]
        return len(canciones)

class Genero(Enum):
    ROCK = 'Rock'
    CLASICA = 'Clasica'
    TROPICAL = 'Tropical'

class Cancion:

    def __init__(self, nombre: str, artista: "Artista", genero: "Genero") -> None:
        self.__nombre = nombre
        self.__artista = artista
        self.__genero = genero

        self.__artista.add_cancion(self)

    @property
    def artista(self) -> "Artista":
        return self.__artista
    
class Artista(Persona):

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__canciones: List["Cancion"] = []

    def add_cancion(self, cancion: "Cancion") -> bool:
        self.__canciones.append(cancion)
        return True
    
class Invitado(Persona):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__emisiones: List["Emision"] = []

    def add_emision(self, emision: "Emision") -> bool:
        self.__emisiones.append(emision)
        return True

def main() -> None:
    radio = RockRollRadio()

    radio.add_locutor(Locutor('Pedro Rock'))
    radio.add_locutor(Locutor('Pablo Clásico'))
    radio.add_locutor(Locutor('Simona Tropical'))
    radio.add_locutor(Locutor('Carolina Marel'))
    
    radio.add_programa(Programa('Great Rock', radio.locutores[0]))
    radio.add_programa(Programa('Las 40 clásicas', radio.locutores[1]))
    radio.add_programa(Programa('Pa la Tropicalle', radio.locutores[2]))
    radio.add_programa(Programa('De todito', radio.locutores[3]))

    radio.add_artista(Artista('Muse'))
    radio.add_cancion(Cancion('Starlight', radio.artistas[0], Genero.ROCK))
    radio.add_cancion(Cancion('Uprising', radio.artistas[0], Genero.ROCK))

    radio.add_artista(Artista('Ludwig van Beethoven'))
    radio.add_cancion(Cancion('Sonata Clara de Luna', radio.artistas[1], Genero.CLASICA))
    radio.add_cancion(Cancion('Fur Elise', radio.artistas[1], Genero.CLASICA))

    radio.add_artista(Artista('Carlos Vives'))
    radio.add_cancion(Cancion('Fruta fresca', radio.artistas[2], Genero.TROPICAL))
    radio.add_cancion(Cancion('Robarte un beso', radio.artistas[2], Genero.TROPICAL))

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('James Hetfield'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('Los de Adentro'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[0]))
    radio.add_invitado(Invitado('Carlos Santana'), radio.programas[0].get_last_emision())
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[0].get_last_emision().add_cancion(radio.canciones[1])

    radio.add_emision(Emision(radio.programas[1]))
    radio.add_invitado(Invitado('Alexis Trejos'), radio.programas[1].get_last_emision())
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[1]))
    radio.add_invitado(Invitado('Julian Navarro'), radio.programas[1].get_last_emision())
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[1].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Checo Acosta'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Fonseca'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[2]))
    radio.add_invitado(Invitado('Bacilos'), radio.programas[2].get_last_emision())
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[2].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[1])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[2])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[5])

    radio.add_emision(Emision(radio.programas[3]))
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[3])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[4])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[0])
    radio.programas[3].get_last_emision().add_cancion(radio.canciones[1])
    
    for artista in radio.artistas:
        print(
            f'El programa que más ha puesto canciones del artista {artista.nombre} es',
            f'{radio.get_programa_con_mas_canciones_de_artista(artista).nombre}'
        )

if __name__ == '__main__':
    main()
