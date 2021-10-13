'''
Este codigo estima en pantalla
la probabilidad de que un entero 
elegido al azar sea un numero perfecto.

Parametros de entrada:
 n = numero que determina hasta que N quiero mi espacio muestral

Autor : Maria Camila Perez Hincapie
Ultima actualizacion: 13 de Octubre, 2021

'''
import random

#definimos una funcion para saber si un numero es entero o no
def perfecto(n):

    x = 2
    perfecto= 0 # se suma los divisores de x
    
    while x <= n:

        if n % x == 0:
            perfecto += n/x
        x += 1
        
    if perfecto == n:
       return True
    else:
        return False

perfecto(3)

#definimos una funcion que nos calcule el numero de numeros perfectos <= x
def v(x):
   
    sum = 0

    for i in range(1,x):
        
        if perfecto(i) == True:
            sum += 1
            prob = sum / x

    return prob

#el valor teorico de P(A) es:
valor_teorico = v(1000)
print(valor_teorico)

#simulacion para estimar P(A)
def P(A):
    
    sum = 0

    for i in range(A):
            x = random.randint(1,A)
            
            if perfecto(x) == True:
                sum += 1
                prob = sum / A

    return prob

P(1000)

if __name__ == '_main_':

 #Espacio muestral para N muy grandes
 muestra = v(1000)/1000
 print(muestra)

'''

Respuesta: Cuando el espacio muestral cambia a N muy grande, P(A) decrementa,
es decir a medida que N aumenta, el evento A := {n es un numero perfecto} se reduce. 
La probabilidad de que el evento suceda se vuelve cada vez mas remota.

'''



