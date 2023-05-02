# **Plan:**

## **Clases Generales:**
- RockRollRadio (🎧)
- Locutor (🎤)
- Programa (📻)
- Persona (👤)
- Invitado (👥)
- Emisión (🎙️)
- Género (🎶)
- Canción (🎵)
- Artista (🎸)

## **Clases, Atributos, Metodos y analisis**
**RockRollRadio**
- Init: No hay entradas
- Atributos:
  - artistas (privado) (lista de Artista)
  - canciones (privado) (lista de Canción)
  - invitados (privado) (lista de Invitado)
  - locutores (privado) (lista de Locutor)
  - programas (privado) (lista de Programa)
- Métodos:
  - add_locutor | params: locutor (Locutor)
  - add_programa | params: programa (Programa)
  - add_artista | params: artista (Artista)
  - add_cancion | params: cancion (Canción)
  - add_emision  | params: emision (Emision) | No hace nada
  - add_invitado | params: invitado (Invitado), emision (Emisión) | Relacion bidireccional de emision y invitado

**Locutor (Hijo de Persona)**
- Init: nombre (Str) (clase Persona)
- Atributos:
  - programas (privado) (Lista de Programa)
- Métodos:
  - No tiene métodos

**Programa**
- Init: nombre (str), locutor (Locutor) 
- Atributos: Relacion con Locutor
  - nombre (privado) (Str)
  - serial (privado) (Autogenerado)
  - emisiones (privado) (lista de Emisión)
  - locutores (privado) (Solo se recive por init)
- Métodos:
  - get_last_emision | params: No tiene parametros

**Persona**  
- Init: nombre (Str)
- Atributos:
  - nombre (protegido) (Str)
- Métodos:
  - No tiene métodos
  
**Invitado (Hijo de Persona)**
- Init: Nombre (Str) (clase Persona) 
- Atributos:
  - emisiones (privado) (lista de Emisión)
- Métodos:
  - No tiene métodos

**Emisión**
- Init: Programa 
- Atributos: Relación con Programa
  - serial (privado) (Autogenerado)
  - canciones (privado) (lista de Canción)
  - invitados (privado) (lista de Invitado)
  - programa (privado) (Programa)
- Métodos:
  - add_cancion | params: cancion (Canción)

**Género** 
- Atributos:
  - ROCK (público)
  - CLÁSICA (público)
  - TROPICAL (público)

**Canción**
- Init: Nombre (Str), artista (Artista), género (Género) 
- Atributos: Relación con Artista
  - nombre (privado) (Str)
  - artista (privado) (Artista)
  - género (privado) (Género)
- Métodos:
  - No tiene métodos

**Artista (Hijo de Persona)**
- Init: Nombre (Str) (clase Persona)
- Atributos:
  - canciones (privado) (lista de Canción)
- Métodos:
  - No tiene métodos
