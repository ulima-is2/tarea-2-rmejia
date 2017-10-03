# coding=utf-8
import sys

# Se han decidido utilizar los siguientes patrones:
# - Factory
# - Decorator (Exportar compra a XML)
# - Singleton

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Cine:
    instancia = None
    #Patrón singleton
    @classmethod
    def get_instance(cls, nombre_cine):
        if cls.instancia == None:
            if nombre_cine == 'CineStark':
                cls.instancia = CineStark()
            elif nombre_cine == 'CinePlaneta':
                cls.instancia = CinePlaneta()
            else:
                return Cine()
        return cls.instancia

    def listar_peliculas(self):
        pass
    def listar_funciones(self, pelicula_id):
        pass
    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        pass

c = Cine()

class CinePlaneta(Cine):
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []

    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class CineStark(Cine):
    def __init__(self):
        peliculaD = Pelicula(1, 'Desparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

#clase factory
class CineFactory:
    def obtener_cine(self, nombre_cine):
        if nombre_cine == 'CineStark':
            return c.get_instance('CineStark')
        elif nombre_cine == 'CinePlaneta':
            return c.get_instance('CinePlaneta')
        else:
            return None

#clase decorator
def formatear_xml(diccionario):
    cad = '<data>\n'
    for key, value in diccionario.items():
        cad  = cad + '\t<%s>%s</%s>\n' % (key, value, key)
    cad = cad + '</data>\n'
    return cad

def main():
    #instanciamiento del factory:
    factory = CineFactory()

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
                cine = factory.obtener_cine('CinePlaneta')
            elif cine == '2':
                cine = factory.obtener_cine('CineStark')

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
                cine = factory.obtener_cine('CinePlaneta')
            elif cine == '2':
                cine = factory.obtener_cine('CineStark')

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
            ####
            print('¿Desea exportar a formato XML su compra?')
            print('1: Si')
            print('Cualquier otro input: no')
            op2 = input('Opcion: ')
            if op2 == '1':
                convert = {
                    "Codigo:" : codigo_entrada,
                    "Cantidad de entradas: ": cantidad_entradas,
                    "Funcion" : funcion_elegida,
                    "Codigo de la pelicula" : pelicula_elegida
                }
                cad = formatear_xml(convert)
                print(cad)

        elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()
