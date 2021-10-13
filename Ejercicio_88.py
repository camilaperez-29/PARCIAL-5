'''
Este codigo estima en pantalla
la probabilidad de que un entero 
elegido al azar sea libre de cuadrados.

Parametros de entrada:
 n = numero que determina hasta que N quiero mi espacio muestral

Autor : Maria Camila Perez Hincapie
Ultima actualizacion: 13 de Octubre, 2021

'''

import math
import random

#segun el teorema la probabilidad de que un entero elegido al azar sea libre de cuadrados.
Valor_teorico = 6 / (math.pi)**2

#definimos una funcion que estime la probabilidad de que un numero al azar sea libre de cuadrados.
def libre(n):

    sum = 0

    for i in range (n):
        num = random.randint(1,n)
       
        for x in range(2,num):

                if (x**2) % num == 0:
                    num = False
                    break                    
           
        if num != False:
            sum += 1
            probabilidad = sum / n

    return probabilidad

libre(1000)
        
#ejercicio 70
def zeta(n):
    
    #inicio de serie
    sumatoria  = 0

    #inicio de ciclo
    for k in range (1,(n+1)):
        termino   = 1 / ((k)**2)
        sumatoria = sumatoria + termino
      
    return sumatoria

#comparacion 
zeta  = zeta(1000)
libre = libre(1000)

'''
Respuesta: mientras la funcion Zeta de Riemann se aproxima a (pi**2)/6, 
           la funcion Libre se aproxima a 6 / (pi**2)
'''
         
                        
                    


  

    