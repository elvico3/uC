import array
import unittest

class Matrix:
    """
    Clase que representa una matriz.

    Ejemplos:
    >>> matrix = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    >>> print(matrix)
    1   2   3
    4   5   6
    >>> matrix[1, 1]
    5
    >>> matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
    >>> print(matrix + matrix2)
    8   10   12
    14   16   18
    >>> print(matrix * 2)
    2   4   6
    8   10   12
    >>> print(Matrix(2, 2, [[1, 2], [10, 20]]).multiply(matrix2))
    27   30   33
    270   300   330
    """

    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        self.elements = array.array('i', [0] * (rows * cols)) if elements is None else array.array('i', [element for row in elements for element in row])

    def __str__(self):
        return '\n'.join(['   '.join(map(str, self.elements[i:i+self.cols])) for i in range(0, len(self.elements), self.cols)])

    def __getitem__(self, index):
        i, j = index
        return self.elements[i * self.cols + j]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener las mismas dimensiones para la suma.")
        result = Matrix(self.rows, self.cols)
        result.elements = array.array('i', [a + b for a, b in zip(self.elements, other.elements)])
        return result

    def __mul__(self, scalar):
        result = Matrix(self.rows, self.cols)
        result.elements = array.array('i', [element * scalar for element in self.elements])
        return result

    def tolist(self):
        return [self.elements[i:i + self.cols].tolist() for i in range(0, len(self.elements), self.cols)]

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.elements[i * result.cols + j] = sum(self.elements[i * self.cols + k] * other.elements[k * other.cols + j] for k in range(self.cols))
        return result

def intercambiar_filas(A, n_cols, fila1, fila2):
    # Verificar si las filas están dentro del rango válido
    if fila1 < 0 or fila1 >= len(A) / n_cols or fila2 < 0 or fila2 >= len(A) / n_cols:
        return "Índices de fila fuera de rango"
    # Calcular los índices correspondientes en la lista plana A
    inicio_fila1 = fila1 * n_cols
    inicio_fila2 = fila2 * n_cols
    # Intercambiar los elementos de las filas
    for i in range(n_cols):
        A[inicio_fila1 + i], A[inicio_fila2 + i] = A[inicio_fila2 + i], A[inicio_fila1 + i]

def multiplicar_fila_por_numero(A, n_cols, fila, numero):
    # Verificar si la fila está dentro del rango válido
    if fila < 0 or fila >= len(A) / n_cols:
        return "Índice de fila fuera de rango"
    # Calcular el índice correspondiente en la lista plana A
    inicio_fila = fila * n_cols
    # Multiplicar cada elemento de la fila por el número dado
    for i in range(n_cols):
        A[inicio_fila + i] *= numero

def sumar_filas_y_reemplazar(A, n_cols, fila_destino, fila_origen1, fila_origen2):
    # Verificar si las filas están dentro del rango válido
    if fila_destino < 0 or fila_destino >= len(A) / n_cols or fila_origen1 < 0 or fila_origen1 >= len(A) / n_cols or fila_origen2 < 0 or fila_origen2 >= len(A) / n_cols:
        return "Índices de fila fuera de rango"

    # Calcular los índices correspondientes en la lista plana A
    inicio_destino = fila_destino * n_cols
    inicio_origen1 = fila_origen1 * n_cols
    inicio_origen2 = fila_origen2 * n_cols

    # Sumar los elementos de las filas origen y asignar el resultado a la fila destino
    for i in range(n_cols):
        A[inicio_destino + i] = A[inicio_origen1 + i] + A[inicio_origen2 + i]


A_original = array.array('f', [1.0, 2, 3.14,
                10, 13.1, 4.5,
                2.0, 7.5, 6.2])

class TestMatrixMethods(unittest.TestCase):
    def test_matrix_initialization(self):
        matrix = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.cols, 3)
        self.assertEqual(matrix.tolist(), [[1, 2, 3], [4, 5, 6]])

    def test_matrix_addition(self):
        matrix_a = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix_b = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        result = matrix_a + matrix_b
        self.assertEqual(result.tolist(), [[8, 10, 12], [14, 16, 18]])

    def test_scalar_multiplication(self):
        matrix = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        result = matrix * 2
        self.assertEqual(result.tolist(), [[2, 4, 6], [8, 10, 12]])

    def test_matrix_multiplication(self):
        matrix_a = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix_b = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
        result = matrix_a.multiply(matrix_b)
        self.assertEqual(result.tolist(), [[58, 64], [139, 154]])

    def test_intercambiar_filas(self):
        A = A_original[:]
        intercambiar_filas(A, 3, 0, 1)
        self.assertEqual(A, array.array('f', [10, 13.1, 4.5, 1.0, 2, 3.14, 2.0, 7.5, 6.2]))

    def test_multiplicar_fila_por_numero(self):
        A = A_original[:]
        multiplicar_fila_por_numero(A, 3, 1, 2)
        self.assertEqual(A, array.array('f', [1.0, 2, 3.14, 20, 26.2, 9.0, 2.0, 7.5, 6.2]))

    def assertArrayAlmostEqual(self, array1, array2, tol=1e-6):
        self.assertEqual(len(array1), len(array2))
        for val1, val2 in zip(array1, array2):
            self.assertAlmostEqual(val1, val2, delta=tol)

    def test_sumar_filas_y_reemplazar(self):
        A = A_original[:]
        sumar_filas_y_reemplazar(A, 3, 2, 0, 1)
        expected_result = array.array('f', [1.0, 2, 3.14, 10.0, 13.1, 4.5, 11.0, 15.1, 7.64])
        self.assertArrayAlmostEqual(A, expected_result)
if __name__ == '__main__':
    unittest.main()

