from random import shuffle, choice



def Acciones (list):

    jarra1 = list[0]
    jarra2 = list[1]

    lista = (1,2,3,4,5,6)
    shuffle(lista)
    Accion = choice(lista)
   
    if Accion == 1 and jarra1 < 4:
        jarra1 = 4
    if Accion == 2 and jarra2 < 3:
        jarra2 = 3
    if Accion == 3 and jarra1 >= 1:
        jarra1 = 0
    if Accion == 4 and jarra2 >= 1:
        jarra2 = 0
    if Accion == 5 and jarra1 >=1 and jarra2 < 3:
        restante = 3 - jarra2
        if restante >= jarra1: 
            jarra2 = jarra2 + jarra1
            jarra1 == 0
        else: 
            jarra1 = jarra1 - restante
            jarra2 = jarra2 + restante
    if Accion == 6 and jarra2 >= 1 and jarra1 < 4:
        restante = 4 - jarra1
        if restante >= jarra2:
            jarra1 = jarra2 + jarra1
            jarra2 = 0
        else:
            jarra2 = jarra2 - restante
            jarra1 = jarra1 + restante

    list[0] = jarra1
    list[1] = jarra2
    return list


    
    



         


