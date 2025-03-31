from random import shuffle
from Objetos import Nodo 

def SeleccionarA (Nodo):
    
    jarra1 = Nodo.jarra1
    jarra2 = Nodo.jarra2

    lista = [1,2,3,4,5,6]

    shuffle(lista)
    
    switch = False

    i=0

    for i in lista:
        Accion = i
        if Accion == 1 and jarra1 < 4:
            jarra1 = 4
            switch = True
        if Accion == 2 and jarra2 < 3:
            jarra2 = 3
            switch = True
        if Accion == 3 and jarra1 >= 1:
            jarra1 = 0
            switch = True
        if Accion == 4 and jarra2 >= 1:
            jarra2 = 0
            switch = True
        if Accion == 5 and jarra1 >=1 and jarra2 < 3:
            restante = 3 - jarra2
            if restante >= jarra1: 
                jarra2 = jarra2 + jarra1
                jarra1 == 0
            else: 
                jarra1 = jarra1 - restante
                jarra2 = jarra2 + restante
            switch = True
        if Accion == 6 and jarra2 >= 1 and jarra1 < 4:
            restante = 4 - jarra1
            if restante >= jarra2:
                jarra1 = jarra2 + jarra1
                jarra2 = 0
            else:
                jarra2 = jarra2 - restante
                jarra1 = jarra1 + restante
            switch = True
        i += 1

    Nodo(jarra1,jarra2)
    
    return Nodo, switch


    
    



         


