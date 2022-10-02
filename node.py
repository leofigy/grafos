import copy

'''
    Represeta un Nodo del Puzzle i.e 
    - valores []
        2 8 3
        1 6 4
        7 _ 5
    - nivel    = g(u): profundidad en el arbol
    - desorden = h(n): numero de casillas desordenadas
    - costo/evaluacion = f(n) = g(u) + h(n)
    - movimiento = U,D,L,R 
'''

class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def es_valido(self, limit):
        return self.x >= 0 and self.x < limit and self.y >= 0 and self.y < limit
    
    def __str__(self) -> str:
        return "punto (x:{},y:{})\n".format(self.x, self.y)


class Nodo:

    def __str__(self) -> str:
        result = ""
        for row in self.valores:
            result += "{}\n".format(row)
        return result

    def __init__(self, valores, nivel=0, costo = 0, moviento= '', cursor = "*"):
        self.valores = valores
        self.nivel = nivel
        self.costo = costo
        self.movimiento = moviento # U, D, L, R
        self.cursor = cursor

    
    def encontrar_valor(self, valor='*'):
        for i in range(0, len(self.valores)):
            for j in range(0,len(self.valores)):
                if self.valores[i][j] == valor:
                    return i,j

    def barajar(self, A, B):
        ''' A y B son coordenadas en la matriz y tienen que ser validos '''
        if B.es_valido(len(self.valores)):
            nuevos_valores = copy.deepcopy(self.valores)
            nuevos_valores[A.x][A.y], nuevos_valores[B.x][B.y] = nuevos_valores[B.x][B.y], nuevos_valores[A.x][A.y]
            return nuevos_valores
    
    def diferencia_con(self, objetivo):
        numero_de_diferencias = 0
        for i in range(0, len(self.valores)):
            for j in range(0, len(self.valores)):
                if self.valores[i][j] != objetivo[i][j] and self.valores[i][j] != self.cursor:
                    numero_de_diferencias += 1
        
        return numero_de_diferencias


    def crear_hijos(self, valor="*"):
        hijos = []

        coordenas = self.encontrar_valor(valor=valor)
        if not coordenas:
            print("simbolo no encontrado ignorando")
            return hijos
        
        x = coordenas[0]
        y = coordenas[1]

        movimientos = {
            "Up" : Punto(
                x,
                y+1
            ),
            "Down" : Punto(
                x,
                y -1
            ),
            "Left" : Punto(
                x - 1,
                y
            ),
            "Right": Punto(
                x + 1 ,
                y
            )
        }


        for mov in movimientos:
            nuevos_valores = self.barajar(Punto(x,y), movimientos[mov])
            # que el movimiento haya sido valido
            if nuevos_valores:
                hijos.append(
                    Nodo(
                        valores=nuevos_valores,
                        nivel=self.nivel+1,
                        costo=0,
                        moviento=mov
                    )
                )
        return hijos