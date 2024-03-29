# -*- coding: utf-8 -*-
"""elemA_ElvisSalazar_20202005022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oLxmKcfHRxQr9SAEhPsTpnk--25iwhB-

# <font face="Times New Roman">UNIVERSIDAD DISTRITAL FRANCISCO JOSÉ DE CALDAS</font>  
## <font face="Times New Roman">Elvis Salazar Méndez 20202005022</font>  
### <font face="Times New Roman">DISEÑO DIGITAL CON MICROCONTROLADORES</font>  
### <font face="Times New Roman">Docente: GERARDO ALCIDES MUÑOZ QUIÑONES</font>
"""

from sympy import *

from array import array
import copy

def elem(A, i, j):
    # Verificar si i y j están en el rango adecuado
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        return "Índices fuera de rango"
    # Calcular el índice correspondiente en la lista plana A
    index = i * 3 + j
    # Retornar el elemento en la posición calculada
    return A[index]

def intercambiar_filas(A, fila1, fila2):
    # Verificar si las filas están dentro del rango válido
    if fila1 < 0 or fila1 >= 3 or fila2 < 0 or fila2 >= 3:
        return "Índices de fila fuera de rango"
    # Calcular los índices correspondientes en la lista plana A
    inicio_fila1 = fila1 * 3
    inicio_fila2 = fila2 * 3
    # Intercambiar los elementos de las filas
    for i in range(3):
        A[inicio_fila1 + i], A[inicio_fila2 + i] = A[inicio_fila2 + i], A[inicio_fila1 + i]


def multiplicar_fila_por_numero(A, fila, numero):
    # Verificar si la fila está dentro del rango válido
    if fila < 0 or fila >= 3:
        return "Índice de fila fuera de rango"
    # Calcular el índice correspondiente en la lista plana A
    inicio_fila = fila * 3
    # Multiplicar cada elemento de la fila por el número dado
    for i in range(3):
        A[inicio_fila + i] *= numero

def sumar_filas_y_reemplazar(A, fila_destino, fila_origen1, fila_origen2):
    # Verificar si las filas están dentro del rango válido
    if fila_destino < 0 or fila_destino >= 3 or fila_origen1 < 0 or fila_origen1 >= 3 or fila_origen2 < 0 or fila_origen2 >= 3:
        return "Índices de fila fuera de rango"

    # Calcular los índices correspondientes en la lista plana A
    inicio_destino = fila_destino * 3
    inicio_origen1 = fila_origen1 * 3
    inicio_origen2 = fila_origen2 * 3

    # Sumar los elementos de las filas origen y asignar el resultado a la fila destino
    for i in range(3):
        A[inicio_destino + i] = A[inicio_origen1 + i] + A[inicio_origen2 + i]



# Definir el array A
A_original = array('f', [1.0, 2, 3.14,
                10, 13.1, 4.5,
                2.0, 7.5, 6.2])

# Crear una copia de la matriz original
A_intercambiada = copy.copy(A_original)
A_Multiplicada = copy.copy(A_original)
A_suma_reemplazo = copy.copy(A_original)

# Ejemplo de uso
print("Matriz original:")
print(A_original)

# Intercambiar las filas 0 y 2 en la copia
intercambiar_filas(A_intercambiada, 0, 1)

print("\nMatriz con filas intercambiadas:")
print(A_intercambiada)


# Multiplicar la fila 1 por 2.5 en la copia
multiplicar_fila_por_numero(A_Multiplicada, 1, 2.5)

print("\nMatriz con fila multiplicada por 2.5:")
print(A_Multiplicada)

# Sumar la fila 0 y la fila 1 y reemplazar la fila 2 con el resultado
sumar_filas_y_reemplazar(A_suma_reemplazo, 2, 0, 1)

print("\nMatriz con fila 2 reemplazada por la suma de fila 0 y fila 1:")
print(A_suma_reemplazo)

"""## **Ejemplo de Manipulación de Matrices**


En este ejemplo, se muestran diferentes operaciones que se pueden realizar en una matriz utilizando Python. Cada operación se ejecuta sobre una copia de la matriz original para preservar la matriz original sin cambios.

1. **Intercambio de Filas:**

   Primero, se intercambian las filas 0 y 1 de la matriz. Esto se logra utilizando la función `intercambiar_filas`, que toma la matriz y los índices de las filas a intercambiar como argumentos. Posteriormente, se imprime la matriz resultante.

2. **Multiplicación de Fila por un Número:**

   Luego, se multiplica la fila 1 de la matriz por 2.5. Esto se realiza utilizando la función `multiplicar_fila_por_numero`, que toma la matriz, el índice de la fila y el número por el cual multiplicar como argumentos. Después de la operación, se muestra la matriz resultante.

3. **Suma de Filas y Reemplazo:**

   Finalmente, se suman las filas 0 y 1 y se reemplaza la fila 2 con el resultado de la suma. Esta operación se lleva a cabo con la función `sumar_filas_y_reemplazar`, que toma la matriz, el índice de la fila destino y los índices de las filas a sumar como argumentos. Después de la operación, se imprime la matriz resultante.

##**Demostracion con Sympy**

Para demostrar que lo anterior concuerda, crearemos la misma matriz usando la libreria de sympy y haremos los mismos cambios demostrando que esta correcto.
"""

M

import copy
from sympy import Matrix

# Definir la matriz original
M = Matrix([[1.0, 2.0, 3.14], [10, 13.1, 4.5], [2.0, 7.5, 6.2]])

# Hacer una copia profunda de M
M_original = copy.deepcopy(M)

# Imprimir la matriz original
print("\nMatriz original:")
print(M_original)
print("")

# Intercambiar filas 0 y 1
M_intercambiada = M.copy()
M_intercambiada.row_swap(0, 1)

# Imprimir la matriz intercambiada
print("Matriz intercambiada:")
print(M_intercambiada)

# Multiplicar la fila 1 por 2.5
M_multiplicada = M_original.copy()  # Utiliza la copia profunda de M original
M_multiplicada[1, :] *= 2.5

# Imprimir la matriz multiplicada
print("\nMatriz multiplicada:")
print(M_multiplicada)



# Sumar las filas 0 y 1 y reemplazar la fila 2 con el resultado
M_suma = M_original.copy()  # Utiliza la copia profunda de M original
suma_filas_01 = M_suma.row(0) + M_suma.row(1)
M_suma.row_del(2)
M_suma = M_suma.row_insert(2, suma_filas_01)

# Imprimir la matriz con la fila 2 reemplazada por la suma de las filas 0 y 1
print("\nMatriz con la fila 2 reemplazada por la suma de las filas 0 y 1:")
print(M_suma)

"""Como podemos ver, este resultado corresponde al obtenido usando las funciones creadas `intercambiar_filas`, `multiplicar_fila_por_numero` y `sumar_filas_y_reemplazar`."""