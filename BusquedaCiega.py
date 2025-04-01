import sys
import random
# Clase Nodo
class Nodo:
    def __init__(self, jarra4, jarra3, anterior=None):
        self.jarra4 = jarra4  # Cantidad de agua en la jarra de 4 litros
        self.jarra3 = jarra3  # Cantidad de agua en la jarra de 3 litros
        self.anterior = anterior  # Nodo anterior para rastrear el camino
    def __str__(self):
      return f"({self.jarra4} {self.jarra3})"  # Representación legible del nodo

# Función para realizar las acciones posibles
def Acciones(nodo):
    sucesores = []
    jarra1 = nodo.jarra4
    jarra2 = nodo.jarra3

    # Acción 1: Llenar la jarra de 4
    if jarra1 < 4:
        sucesores.append(Nodo(4, jarra2, nodo))
    
    # Acción 2: Llenar la jarra de 3
    if jarra2 < 3:
        sucesores.append(Nodo(jarra1, 3, nodo))
    
    # Acción 3: Vaciar la jarra de 4
    if jarra1 > 0:
        sucesores.append(Nodo(0, jarra2, nodo))

    # Acción 4: Vaciar la jarra de 3
    if jarra2 > 0:
        sucesores.append(Nodo(jarra1, 0, nodo))

    # Acción 5: Volcar de la jarra de 4 a la jarra de 3
    if jarra1 > 0 and jarra2 < 3:
        restante = 3 - jarra2
        if restante >= jarra1:
            sucesores.append(Nodo(0, jarra2 + jarra1, nodo))
        else:
            sucesores.append(Nodo(jarra1 - restante, 3, nodo))

    # Acción 6: Volcar de la jarra de 3 a la jarra de 4
    if jarra2 > 0 and jarra1 < 4:
        restante = 4 - jarra1
        if restante >= jarra2:
            sucesores.append(Nodo(jarra2 + jarra1, 0, nodo))
        else:
            sucesores.append(Nodo(4, jarra2 - restante, nodo))

    return sucesores

# Función para evaluar si el nodo es el estado deseado
def Evaluar(nodo):
    return nodo.jarra4 == 2  # El objetivo es tener 2 litros en la jarra de 4 litros

# Algoritmo de búsqueda por anchura
def BusquedaCiega(jarra1, jarra2):
    nodo_inicial = Nodo(jarra1, jarra2)
    
    abiertos = [nodo_inicial]  # Lista de nodos abiertos
    cerrados = []  # Usamos una lista para los nodos cerrados
    camino = []  # Para reconstruir el camino

    numero_de_nodo = 0  # Contador de nodos explorados

    # Título de las columnas
    print("Nodo Actual Sucesores Abiertos")

    while abiertos:
        random.shuffle(abiertos)
        nodo = abiertos.pop(0)  # Extraemos el primer nodo de la lista de abiertos

        # Mostrar el nodo actual y los sucesores de una manera adecuada
        sucesores = Acciones(nodo)

        # Imprimir el estado actual
        # Modifica la impresión para que se vea bien
        print(f"{numero_de_nodo} {nodo} { [str(s) for s in sucesores] } { [str(a) for a in abiertos] }")

        # Generar los sucesores del nodo actual
        for sucesor in sucesores:
            # Verificar si el sucesor ya fue visitado (ya está en cerrados o en abiertos)
            if not any(sucesor.jarra4 == n.jarra4 and sucesor.jarra3 == n.jarra3 for n in cerrados) and \
               not any(sucesor.jarra4 == n.jarra4 and sucesor.jarra3 == n.jarra3 for n in abiertos):
                abiertos.append(sucesor)

        # Agregar el nodo actual a los cerrados
        cerrados.append(nodo)

        # Verificar si el nodo actual es el objetivo
        if Evaluar(nodo):
            # Si encontramos el objetivo, reconstruimos el camino
            while nodo:
                camino.append(str(nodo))  # Añadir la representación del nodo, no el objeto
                nodo = nodo.anterior
            camino.reverse()  # Revertir el camino
            print(f"Camino: {', '.join(camino)}")  # Mostrar el camino como lista de nodos
            return

        numero_de_nodo += 1

# Ejemplo de ejecución

try:
      jarra1 = int(sys.argv[1])
      jarra2 = int(sys.argv[2])

      if jarra1 > 4 or jarra2 > 3:

            raise ValueError("Error, la jarra no puede estar tan llena")
      
except ValueError as e:

      print(e)
else:
    BusquedaCiega(jarra1,jarra2)
