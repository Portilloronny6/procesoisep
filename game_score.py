class Puntuaciones():

    def __init__(self):
        self.lista = []

    def ingresar_puntuaciones(self):
        while True:
            n = float(input('Ingresar puntuación: '))
            self.lista.append(n)
            condicion = int(
                input('\nPresiona "1" Para continuar agregando puntuaciones. Sino, presiona "2".--> '))
            if condicion == 1:
                continue
            else:
                break
        return self.lista

    def __str__(self):
        return f'{self.lista}'

    def mas_alta(self):
        if len(self.lista) == 0:
            print("La lista de puntuaciones esta vacía.")
        else:
            return max(self.lista)

    def ultima_puntuacion(self):
        if len(self.lista) == 0:
            print("La lista de puntuaciones esta vacía.")
        else:
            return self.lista[-1]

    def tres_mas_altas(self):
        if len(self.lista) == 0:
            print("La lista de puntuaciones esta vacía.")
        else:
            lista = sorted(self.lista, reverse=True)
            return lista[:3]
