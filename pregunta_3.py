# coding=utf-8
import sys
#Se agregó conectividad con la base de datos para descargar de ahí las funciones y peliculas.
import sqlite3
conn = sqlite3.connect('pregunta3.db')

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class dataDAO:
    def __init__(self):
        self.id_p = None
        self.id_pel = None

    def get_peliculas(self, id_p):
        self.id_p = id_p
        cur = conn.cursor()
        cur.execute("select  p.id_Pelicula, nombre from T_Pelicula  p join T_PeliculaxCine where id_Cine = ? group by p.id_Pelicula", id_p)
        rows = cur.fetchall()

        arr_pel = []
        for row in rows:
            #print(row)
            pel = Pelicula(row[0],row[1])
            #print(pel)
            arr_pel.append(pel)

        return arr_pel

    def get_funciones(self, id_pel):
        self.id_pel = id_pel
        cur = conn.cursor()
        cur.execute("select  nombre from T_Funcion  f join T_PeliculaxCine where f.id_Pelicula = ? group by f.id_Funcion", id_pel)
        rows = cur.fetchall()

        arr_fun = []
        for row in rows:
            #print(row)
            fun = row[0]
            arr_fun.append(fun)

        return arr_fun

class CinePlaneta:
    def __init__(self):

        dao = dataDAO()
        id_p = "1"
        arr_pel = dao.get_peliculas(id_p)

        for pel in arr_pel:
            #print(str(pel.id))
            pel.funciones = dao.get_funciones(str(pel.id))

        self.lista_peliculas = arr_pel
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)



class CineStark:
    def __init__(self):
        dao = dataDAO()
        id_p = "2"
        arr_pel = dao.get_peliculas(id_p)

        for pel in arr_pel:
            #print(str(pel.id))
            pel.funciones = dao.get_funciones(str(pel.id))

        self.lista_peliculas = arr_pel
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

def main():
    terminado = False;
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()
