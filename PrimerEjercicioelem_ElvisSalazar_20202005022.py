from array import array

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
        
        
# Definir el array A
A = array('f', [1.0, 2, 3.14,
                float('inf'), float('nan'), 4.5,
                2.0, 7.5, 6.2])

# Ejemplo de uso
print("Matriz original:")
print(A)

# Intercambiar las filas 0 y 2
intercambiar_filas(A, 0, 1)

print("\nMatriz con filas intercambiadas:")
print( A)


multiplicar_fila_por_numero(A, 1, 2.5)

print("\nMatriz con fila multiplicada por 2.5:")
print(A)

