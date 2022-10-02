from node import Nodo

class Puzzle:
    def __init__(self):
        self.por_visitar = []
        self.visitados = []

    
    def resolver(self, inicial, objetivo):

        inicio = Nodo(valores=inicial)
        inicio.costo = inicio.diferencia_con(objetivo) + inicio.nivel

        self.por_visitar.append(inicio)

        while True:
            if len(self.por_visitar) == 0:
                print("nada que hacer ....")
                break

            actual = self.por_visitar[0]

            print ("Nodo actual\n", actual)

            if actual.diferencia_con(objetivo) == 0:
                print("lo resolvimos !!!")
                break

            for nodo_expandido in actual.crear_hijos():
                print("vamos a expandir ....")
                nodo_expandido.costo = nodo_expandido.diferencia_con(objetivo) + nodo_expandido.nivel
                self.por_visitar.append(nodo_expandido)
            
            self.visitados.append(actual)
            del self.por_visitar[0]

            self.por_visitar.sort(
                key = lambda x:x.costo, reverse=False
            )