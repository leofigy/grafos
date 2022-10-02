from puzzle import Puzzle

def leer_valores(puzzle_size=3, cursor="*"):
    matriz = []
    tiene_cursor = 0
    for i in range(puzzle_size):
        print ("> Ingresa fila ", i + 1)
        while True:
            linea = input().strip().split(" ")
            if not (len(linea)  == puzzle_size):
                print("ignorando linea vuelva a ingresar, mal tamaño", len(linea))
                continue
            
            matriz.append(linea)
            # buscando el cursor por si las dudas
            if cursor in linea:
                tiene_cursor += 1 
            break
    
    if tiene_cursor != 1:
        print("revisa la entrada solo se necesita un cursor", matriz)
        if tiene_cursor == 0:
            print("no hay cursor")
        if tiene_cursor > 1:
            print("hay mas que un cursor")
        exit(1)

    
    return matriz


if __name__ == '__main__':
    #print ("****************** Nestor Puzzle ******************")
    #print("caracter por defecto casilla = * (Asterisco)")
    #print ("Puzzle inicial: ")
    #inicial = leer_valores()
    #print("******************* Puzzle objetivo : **************")
    #objetivo = leer_valores()

    #solucionable
    #inicial = [ [2, 8, 3] , [1, 6, 4] , [7, '*', 5]]
    #objetivo = [ [1, 2, 3] , [8 , "*", 4], [7, 6, 5]]

    # no solucionable

    objetivo = [
        [1,2,3],
        [4,5,6],
        [7,8, "*"]
    ]

    inicial = [
        [1,2,3],
        [4, 5,7],
        [6,8, "*"]
    ]   



    mi_puzzle = Puzzle() # 3x3 - 1 cursor
    mi_puzzle.resolver(inicial, objetivo)



