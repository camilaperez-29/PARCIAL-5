# PARCIAL-5
Números Perfectos

En este repositorio encontraras el desarrollo de  2 ejercicios basados en numeros
aleatorios y probabilidad, con el fin de poner en práctica los conocimientos adquiridos
en la ultima unidad del curso de computacion Udea.

## COMENCEMOS 🚀
-----
### **PROBLEMA1**

Un teorema afirma que

 *la probabilidad de que un entero elegido al azar sea libre de cuadrado es*
 
 $$\frac{6}{\pi^2}$$

 Realice una simulacion para estimar el valor teorico de la probabilidad enunciado en el teorema $\frac{6}{\pi^2}$. Compare con el ejercicio (70).(*sugerencia:* suponga que los enteros positivos son finitos: $\mathbb{Z}^+ $= {1,...N} con N muy "grande").

 ### *solucion*:

- Primero: importamos librerias

    ``` 
        import math
        import random
    ```

- segundo = definamos la función `libre(n) ` la cual estima la probabilidad de que un entero escogido al azar sea libre de cuadrados en el lenguaje de Python.


``` 
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

```
- Tercero: Comaparamos con la funcion `zeta(n)`, el valor teorico del teorema y la funcion `libre(n)`

```
def zeta(n):
    
    #inicio de serie
    sumatoria  = 0

    #inicio de ciclo
    for k in range (1,(n+1)):
        termino   = 1 / ((k)**2)
        sumatoria = sumatoria + termino
      
    return sumatoria
```
```
  Valor_teorico= 6/(math.pi)**2
   
  #comparacion 
    zeta  = zeta(1000)
    libre = libre(1000)

```
### **RESPUESTA:** 📌
mientras la funcion Zeta de Riemann se aproxima a $\frac{\pi^2}{6}$, la funcion Libre se aproxima a $\frac{6}{\pi^2}$