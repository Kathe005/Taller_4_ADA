# Ejercicio 1. Suma de un arreglo
def suma_arreglo(arr):
    
    if len(arr) == 1: #caso base 
        return arr[0]
          
    mid = len(arr) // 2      #Dividimos en 2 mitades 
    izquierda = suma_arreglo(arr[:mid])
    derecha = suma_arreglo(arr[mid:])

    return izquierda + derecha # combina los resultados


print("  ")
print("Suma:", suma_arreglo([1, 2, 3, 4, 5]))


# Ejercicio 2: Busqueda del Máximo y Mínimo
def max_min(arr):

    # Caso base
    if len(arr) == 1:
        return arr[0], arr[0]
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    

    mid = len(arr) // 2 # Dividimos tambien en dos mitades
    min_izq, max_izq = max_min(arr[:mid])
    min_der, max_der = max_min(arr[mid:])
    
    return min(min_izq, min_der), max(max_izq, max_der) # combina los resultados

print("Min y Max:", max_min([3, 1, 7, 9, 2]))


# Ejercicio 3: multiplicacion de enteros (karatsuba)
def karatsuba(x, y):
    # Convertimos a string para manejar dígitos
    x, y = str(x), str(y)
    n = max(len(x), len(y))
    
    # Caso base
    if n == 1:
        return int(x) * int(y)
    
    # Ajustamos longitud
    x, y = x.zfill(n), y.zfill(n)
    m = n // 2
    
    # Dividimos números
    x1, x0 = int(x[:-m]), int(x[-m:])
    y1, y0 = int(y[:-m]), int(y[-m:])
    
    # Recursión
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    
    return (z2 * 10**(2*m)) + (z1 * 10**m) + z0


print("Karatsuba:", karatsuba(1234, 5678))


# Ejercicio 4: Potenciación Rápida

def potencia_rapida(a, b):
    if b == 0:
        return 1
    mitad = potencia_rapida(a, b // 2)
    if b % 2 == 0:
        return mitad * mitad
    else:
        return mitad * mitad * a


print("Potencia rápida:", potencia_rapida(2, 10))

# Ejercicio 5: Ordenacion con Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])
    
    return merge(izquierda, derecha)

def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


print("Merge Sort:", merge_sort([5, 2, 9, 1, 7]))


# Ejercicio 6: Multiplicacion de matrices con strassen

import numpy as np

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    # Dividimos matrices en submatrices
    A11, A12, A21, A22 = dividir(A, mid)
    B11, B12, B21, B22 = dividir(B, mid)
    
    # Calculamos productos de Strassen
    M1 = strassen(sumar(A11, A22), sumar(B11, B22))
    M2 = strassen(sumar(A21, A22), B11)
    M3 = strassen(A11, restar(B12, B22))
    M4 = strassen(A22, restar(B21, B11))
    M5 = strassen(sumar(A11, A12), B22)
    M6 = strassen(restar(A21, A11), sumar(B11, B12))
    M7 = strassen(restar(A12, A22), sumar(B21, B22))
    
    # Combinamos resultados
    C11 = sumar(restar(sumar(M1, M4), M5), M7)
    C12 = sumar(M3, M5)
    C21 = sumar(M2, M4)
    C22 = sumar(restar(sumar(M1, M3), M2), M6)
    
    return combinar(C11, C12, C21, C22)

def dividir(M, mid):
    return ( [row[:mid] for row in M[:mid]],
             [row[mid:] for row in M[:mid]],
             [row[:mid] for row in M[mid:]],
             [row[mid:] for row in M[mid:]] )

def sumar(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def restar(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def combinar(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Strassen:", strassen(A, B))

# Ejercicio 7: Busqueda en una matriz ordenada 

def buscar_matriz_ordenada(matriz, x):
    n = len(matriz)
    fila, col = 0, n - 1
    
    while fila < n and col >= 0:
        if matriz[fila][col] == x:
            return True
        elif matriz[fila][col] > x:
            col -= 1  # descartamos columna
        else:
            fila += 1  # descartamos fila
    return False


matriz = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

print("Buscar 9:", buscar_matriz_ordenada(matriz, 9))
print("Buscar 15:", buscar_matriz_ordenada(matriz, 15))

 

#Ejercicio Big O: Algoritmo misteri

def misteri(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print("  ")
print("Factorial de 5:", misteri(5))  
print("Factorial de 10:", misteri(10)) 
print("factorial de 3: ", misteri (3))
# R// Este algoritmo lo que hace es calcular el factorial de n, el bucle for se repite 
# n-1 veces, y en cada vuelta hace una multiplicacion por eso el  
# algoritmo es lineal y su complejidad es osea O(n) por que el ciclo se ejecuta 
# n de veces.