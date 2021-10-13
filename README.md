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


### **PROBLEMA2**

Se elige al azar un entero n $\in \Omega:=$ {1,...N} con N := 100 y deseamos estudiar el evento A 
$:=$ {n es un numero perfecto}

a) utilice la funcion $V(x)$ para hallar el valor teorico de $P(A)$

```
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
```
```
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
```

b) Realice una simulacion para estimar el valor teorico de $P(A)$ obtenido en $(a)$

```
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

```
c) ¿ Que ocurre cuando el espacio muestral $\Omega $ cambia y $N=1000, N=10000, N=100000$


```
 #Espacio muestral para N muy grandes
 muestra = v(1000)/1000
 print(muestra)
```
### **RESPUESTA:** 📌
Cuando el espacio muestral cambia a N muy grande, P(A) decrementa,
es decir a medida que N aumenta, el evento A := {n es un numero perfecto} se reduce. 
La probabilidad de que el evento suceda se vuelve cada vez mas remota.