from calendar import c
import node

def test_crear_nodo():
    valores = [ [2, 8, 3] , [1, 6, 4] , [7, '*', 5]]

    miNodo = node.Nodo(valores)
    coordenadas = miNodo.encontrar_valor()
    assert len(coordenadas) == 2
    assert coordenadas[0] == 2
    assert coordenadas[1] == 1
    print(coordenadas)

    print("root: \n", miNodo)

    hijos = miNodo.crear_hijos()
    for hijo in hijos:
        print(hijo)
        print("-----------")
