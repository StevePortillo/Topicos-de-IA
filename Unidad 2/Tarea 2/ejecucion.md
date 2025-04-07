Configuración del algoritmo de Búsqueda Tabú para el problema de las 8 reinas:
Ingrese la tenencia Tabú : 9
Ingrese el número máximo de iteraciones : 100
Ingrese el tamaño del vecindaro: 8
Ingrese la solución inicial: 0 1 2 3 4 5 6 7  

--- Inicio de la búsqueda ---
Solución inicial: [0, 1, 2, 3, 4, 5, 6, 7], Coste: 28

Iteración 1
Solución actual: [0, 1, 7, 3, 4, 5, 6, 7]
Conflictos actuales: 22
Mejor solución encontrada: [0, 1, 7, 3, 4, 5, 6, 7]
Mejor costo : 22
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7]]

Iteración 2
Solución actual: [0, 1, 7, 3, 4, 2, 6, 7]
Conflictos actuales: 16
Mejor solución encontrada: [0, 1, 7, 3, 4, 2, 6, 7]
Mejor costo : 16
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7]]

Iteración 3
Solución actual: [0, 1, 7, 3, 0, 2, 6, 7]
Conflictos actuales: 12
Mejor solución encontrada: [0, 1, 7, 3, 0, 2, 6, 7]
Mejor costo : 12
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7]]

Iteración 4
Solución actual: [6, 1, 7, 3, 0, 2, 6, 7]
Conflictos actuales: 9
Mejor solución encontrada: [6, 1, 7, 3, 0, 2, 6, 7]
Mejor costo : 9
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7]]

Iteración 5
Solución actual: [6, 1, 7, 3, 0, 2, 0, 7]
Conflictos actuales: 8
Mejor solución encontrada: [6, 1, 7, 3, 0, 2, 0, 7]
Mejor costo : 8
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7]]        

Iteración 6
Solución actual: [6, 1, 7, 3, 0, 2, 4, 7]
Conflictos actuales: 5
Mejor solución encontrada: [6, 1, 7, 3, 0, 2, 4, 7]
Mejor costo : 5
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7]]

Iteración 7
Solución actual: [6, 3, 7, 3, 0, 2, 4, 7]
Conflictos actuales: 5
Mejor solución encontrada: [6, 1, 7, 3, 0, 2, 4, 7]
Mejor costo : 5
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7]]

Iteración 8
Solución actual: [6, 3, 7, 3, 0, 2, 4, 6]
Conflictos actuales: 4
Mejor solución encontrada: [6, 3, 7, 3, 0, 2, 4, 6]
Mejor costo : 4
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6]]

Iteración 9
Solución actual: [6, 0, 7, 3, 0, 2, 4, 6]
Conflictos actuales: 4
Mejor solución encontrada: [6, 3, 7, 3, 0, 2, 4, 6]
Mejor costo : 4
Lista Tabú: [[0, 1, 7, 3, 4, 5, 6, 7], [0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6]]

Iteración 10
Solución actual: [1, 0, 7, 3, 0, 2, 4, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 0, 7, 3, 0, 2, 4, 6]
Mejor costo : 3
Lista Tabú: [[0, 1, 7, 3, 4, 2, 6, 7], [0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6]]

Iteración 11
Solución actual: [1, 5, 7, 3, 0, 2, 4, 6]
Conflictos actuales: 1
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[0, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6]]

Iteración 12
Solución actual: [1, 5, 7, 5, 0, 2, 4, 6]
Conflictos actuales: 1
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 1, 7, 3, 0, 2, 6, 7], [6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6]]

Iteración 13
Solución actual: [1, 5, 7, 2, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 1, 7, 3, 0, 2, 0, 7], [6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6]]

Iteración 14
Solución actual: [1, 5, 7, 0, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 1, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6]]

Iteración 15
Solución actual: [1, 5, 7, 6, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 3, 7, 3, 0, 2, 4, 7], [6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6]]

Iteración 16
Solución actual: [1, 5, 1, 6, 0, 2, 4, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 3, 7, 3, 0, 2, 4, 6], [6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6]]

Iteración 17
Solución actual: [1, 5, 3, 6, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[6, 0, 7, 3, 0, 2, 4, 6], [1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6]]

Iteración 18
Solución actual: [1, 5, 3, 6, 0, 2, 4, 7]
Conflictos actuales: 1
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 0, 7, 3, 0, 2, 4, 6], [1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7]]

Iteración 19
Solución actual: [1, 7, 3, 6, 0, 2, 4, 7]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 7, 3, 0, 2, 4, 6], [1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7]]

Iteración 20
Solución actual: [1, 7, 3, 6, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 7, 5, 0, 2, 4, 6], [1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6]]

Iteración 21
Solución actual: [1, 7, 3, 5, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 7, 2, 0, 2, 4, 6], [1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6]]

Iteración 22
Solución actual: [0, 7, 3, 5, 0, 2, 4, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 7, 0, 0, 2, 4, 6], [1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6]]

Iteración 23
Solución actual: [0, 7, 3, 5, 0, 2, 1, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 7, 6, 0, 2, 4, 6], [1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6]]

Iteración 24
Solución actual: [0, 7, 3, 7, 0, 2, 1, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 1, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6]]

Iteración 25
Solución actual: [0, 7, 3, 7, 0, 3, 1, 6]
Conflictos actuales: 4
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 3, 6, 0, 2, 4, 6], [1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6]]

Iteración 26
Solución actual: [0, 7, 3, 6, 0, 3, 1, 6]
Conflictos actuales: 4
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 5, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6]]

Iteración 27
Solución actual: [0, 2, 3, 6, 0, 3, 1, 6]
Conflictos actuales: 4
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 7, 3, 6, 0, 2, 4, 7], [1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6]]

Iteración 28
Solución actual: [0, 2, 4, 6, 0, 3, 1, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 7, 3, 6, 0, 2, 4, 6], [1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6]]

Iteración 29
Solución actual: [7, 2, 4, 6, 0, 3, 1, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[1, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6]]

Iteración 30
Solución actual: [5, 2, 4, 6, 0, 3, 1, 6]
Conflictos actuales: 1
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[0, 7, 3, 5, 0, 2, 4, 6], [0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 6, 0, 3, 1, 6]]

Iteración 31
Solución actual: [5, 2, 4, 5, 0, 3, 1, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[0, 7, 3, 5, 0, 2, 1, 6], [0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 5, 0, 3, 1, 6]]

Iteración 32
Solución actual: [5, 2, 7, 5, 0, 3, 1, 6]
Conflictos actuales: 3
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[0, 7, 3, 7, 0, 2, 1, 6], [0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 5, 0, 3, 1, 6], [5, 2, 7, 5, 0, 3, 1, 6]]

Iteración 33
Solución actual: [5, 2, 7, 7, 0, 3, 1, 6]
Conflictos actuales: 2
Mejor solución encontrada: [1, 5, 7, 3, 0, 2, 4, 6]
Mejor costo : 1
Lista Tabú: [[0, 7, 3, 7, 0, 3, 1, 6], [0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 5, 0, 3, 1, 6], [5, 2, 7, 5, 0, 3, 1, 6], [5, 2, 7, 7, 0, 3, 1, 6]]

Iteración 34
Solución actual: [5, 2, 4, 7, 0, 3, 1, 6]
Conflictos actuales: 0
Mejor solución encontrada: [5, 2, 4, 7, 0, 3, 1, 6]
Mejor costo : 0
Lista Tabú: [[0, 7, 3, 6, 0, 3, 1, 6], [0, 2, 3, 6, 0, 3, 1, 6], [0, 2, 4, 6, 0, 3, 1, 6], [7, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 6, 0, 3, 1, 6], [5, 2, 4, 5, 0, 3, 1, 6], [5, 2, 7, 5, 0, 3, 1, 6], [5, 2, 7, 7, 0, 3, 1, 6], [5, 2, 4, 7, 0, 3, 1, 6]]

¡Solución óptima encontrada!

--- Métricas ---
Tiempo de ejecución: 0.0313 segundos
Número de movimientos: 34

Mejor solución encontrada: [5, 2, 4, 7, 0, 3, 1, 6]
Número de colisiones: 0

Tablero de ajedrez con la solucion optima:
. . . . Q . . .
. . . . . . Q .
. Q . . . . . .
. . . . . Q . .
. . Q . . . . .
Q . . . . . . .
. . . . . . . Q
. . . Q . . . . 
