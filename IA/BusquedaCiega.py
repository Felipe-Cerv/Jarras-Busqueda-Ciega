
import sys
import Acciones.Accion as A 
from Objetos import Nodo 

      
def Evaluar():
      if jarra1 == 2:
            return True
      else:
            return False
       
try:
      jarra1 = int(sys.argv[1])
      jarra2 = int(sys.argv[2])

      if jarra1 > 4 or jarra2 > 3:

            raise ValueError("Error, la jarra no puede estar tan llena")
      
except ValueError as e:

      print(e)
else:
      nodo = Nodo(jarra1, jarra2)

      abiertos = []
      cerrados = []
      NuevosS = []

      abiertos.append(nodo)

      Numero_de_nodo=0
      
      while abiertos:
            
            Numero_de_nodo+=1
            Actual = nodo
            cerrados.append(Actual)
            #impresion de los nodos 

            print(Numero_de_nodo)
            print(Actual)
            print(nodo_s)
            print(abiertos)
            #impresion de los nodos 
            
            if Evaluar(Actual) == True:

                  print(Actual)
                  
            else:
                  
                  nodo_s = A.SeleccionarA(Actual)
                  NuevosS.append(Actual.nodos_sucesores)
                  abiertos.append(NuevosS)









