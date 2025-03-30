from queue import Queue
import sys


def busqueda (jarra1, jarra2):
       
       nodo = [jarra1,jarra2] 

       abiertos = Queue(maxsize=0)
       cerrados = Queue(maxsize=0)
       
       while not abiertos.empty() == True:

         abiertos.put(nodo)
         cerrados.put(nodo)


         if abiertos.empty() == True:
               return cerrados(nodo)
         else:
                








